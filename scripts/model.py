import datetime
import re

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from constants import (
    JSONInputKeys, YAMLScheduleKeys, SessionOutputFields, TalkOutputFields
)


def assert_fields_in_dictionary(required_fields: List[str], data: Dict[str, Any]) -> None:
    """
    Assert that all required fields are present in the dictionary.
    
    Args:
        required_fields: List of field names that must be present in data
        data: Dictionary to check
        
    Raises:
        ValueError: If any required field is missing from data
    """
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: '{field}'")


@dataclass
class FHSchedule:
    """Represents the Friday Hacks schedule for a semester."""
    start_nr: int
    start_date: datetime.date
    hacks: List[Dict[str, Any]]

    def __str__(self) -> str:
        """Return a human-readable string representation of the schedule."""
        return f"FHSchedule(start_nr={self.start_nr}, start_date={self.start_date}, hacks_count={len(self.hacks)})"

    def to_dict(self) -> Dict[str, Any]:
        """Convert the FHSchedule instance to a dictionary format for YAML serialization."""
        return {
            YAMLScheduleKeys.START_DATE: self.start_date.strftime("%Y-%m-%d") + " 19:00:00 +0800",
            YAMLScheduleKeys.START_NR: self.start_nr,
            YAMLScheduleKeys.HACKS: self.hacks
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FHSchedule":
        """
        Create an FHSchedule from a dictionary.

        Args:
            data: Dictionary with keys: start_nr, start_date (string like "YYYY-MM-DD HH:MM:SS +HHMM"), and hacks

        Returns:
            FHSchedule instance

        Raises:
            ValueError: If any required field is missing
        """
        assert_fields_in_dictionary([YAMLScheduleKeys.START_NR, YAMLScheduleKeys.START_DATE, YAMLScheduleKeys.HACKS], data)

        # Parse start_date string (format: "YYYY-MM-DD HH:MM:SS +HHMM")
        start_date_str = data[YAMLScheduleKeys.START_DATE]
        # Extract just the date part
        date_part = start_date_str.split()[0]
        start_date = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()

        return cls(
            start_nr=data[YAMLScheduleKeys.START_NR],
            start_date=start_date,
            hacks=data[YAMLScheduleKeys.HACKS]
        )

    def update_session(self, week_number: int, session_details: Dict[str, Any]) -> None:
        """
        Update the schedule with the details of a specific session.

        Args:
            week_number: The week number to update (int)
            session_details: A dictionary containing the session details to update in the schedule
        """
        index = week_number - self.start_nr
        if 0 <= index < len(self.hacks):
            self.hacks[index] = session_details
        else:
            raise IndexError(f"Week number {week_number} is out of range for the schedule starting at {self.start_nr} with {len(self.hacks)} sessions.")

    def update_by_date(self, date: datetime.date, session_details: Dict[str, Any]) -> None:
        """
        Update the schedule with session details based on the session date.
        Calculates the week number from the date relative to the schedule's start date.

        Args:
            date: The date of the session (datetime.date)
            session_details: A dictionary containing the session details to update in the schedule
        """
        # Calculate weeks from start_date to the given date
        weeks_from_start = (date - self.start_date).days // 7
        week_number = self.start_nr + weeks_from_start
        self.update_session(week_number, session_details)


@dataclass
class FHTalk:
    """Represents a single talk at a Friday Hacks session."""
    speaker: str
    title: str
    description: str
    poster_link: str
    start_time: datetime.time
    end_time: datetime.time
    talk_from: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FHTalk":
        """
        Create an FHTalk from a dictionary.

        Args:
            data: Dictionary with keys: speaker, title, description, poster_link, and optional talk_from

        Returns:
            FHTalk instance

        Raises:
            ValueError: If any required field is missing
        """
        assert_fields_in_dictionary([TalkOutputFields.SPEAKER, TalkOutputFields.TITLE, TalkOutputFields.DESCRIPTION, TalkOutputFields.POSTER_LINK, JSONInputKeys.START_TIME, JSONInputKeys.END_TIME], data)

        return cls(
            speaker=data[TalkOutputFields.SPEAKER],
            title=data[TalkOutputFields.TITLE],
            description=data[TalkOutputFields.DESCRIPTION],
            poster_link=data[TalkOutputFields.POSTER_LINK],
            talk_from=data.get(TalkOutputFields.TALK_FROM),
            start_time=data[JSONInputKeys.START_TIME],
            end_time=data[JSONInputKeys.END_TIME]
        )

    def to_schedule_ready_dict(self) -> Dict[str, Any]:
        d = {
            TalkOutputFields.SPEAKER: self.speaker,
            TalkOutputFields.TITLE: self.title,
        }
        if self.talk_from:
            d[TalkOutputFields.TALK_FROM] = self.talk_from
        return d

    def __str__(self) -> str:
        """Return a human-readable string representation of the talk."""
        from_str = f" (from {self.talk_from})" if self.talk_from else ""
        return f"FHTalk(speaker={self.speaker!r}, title={self.title!r}, time={self.start_time}-{self.end_time}{from_str})"


@dataclass
class FHSession:
    """Represents the details of a single Friday Hacks session."""
    session_number: int
    date: datetime.date
    venue: str
    venue_link: str
    no_hack: bool
    no_hack_reason: Optional[str]
    talks: List[FHTalk]
    signup_link: str

    @classmethod
    def _parse_dt(cls, dt_str: str) -> datetime.datetime:
        """Helper to parse JS ISO strings like 2026-05-14T10:00:00.000+08:00"""
        if not dt_str:
            return None
        return datetime.datetime.fromisoformat(dt_str)

    @classmethod
    def _parse_venue_details(cls, venue_str: str) -> Tuple[str, str]:
        """
        Parse the venue string to extract the venue name and link if present.
        Venue string is in markdown link format: [venue](link)
        """
        match = re.match(r"\[(.*?)\]\((.*?)\)", venue_str)
        if match:
            return match.group(1), match.group(2)
        else:
            return venue_str, ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FHSession":
        # Check if this is a no-hack session
        no_hack = data.get(JSONInputKeys.NO_HACK, False)

        # All sessions require date
        if JSONInputKeys.DATE not in data:
            raise ValueError(f"Missing required field: '{JSONInputKeys.DATE}'")

        if no_hack:
            # For no-hack sessions, only date and reason are required
            if not data.get(JSONInputKeys.NO_HACK_REASON):
                raise ValueError(f"{JSONInputKeys.NO_HACK} is True but {JSONInputKeys.NO_HACK_REASON} is missing or empty")

            parsed_date = cls._parse_dt(data[JSONInputKeys.DATE]).date()

            return cls(
                session_number=0,  # Placeholder for no-hack sessions
                date=parsed_date,
                venue="",
                venue_link="",
                no_hack=True,
                no_hack_reason=data[JSONInputKeys.NO_HACK_REASON],
                talks=[],
                signup_link=""
            )
        else:
            # For regular sessions, all fields are required
            assert_fields_in_dictionary([JSONInputKeys.SESSION_NUMBER, JSONInputKeys.VENUE, JSONInputKeys.TALKS, JSONInputKeys.SIGNUP_LINK], data)

            if not data[JSONInputKeys.TALKS]:
                raise ValueError(f"The '{JSONInputKeys.TALKS}' field must be a non-empty list")

            parsed_date = cls._parse_dt(data[JSONInputKeys.DATE]).date()

            parsed_talks = []
            for t in data[JSONInputKeys.TALKS]:
                parsed_t = dict(t)
                if parsed_t.get(JSONInputKeys.START_TIME):
                    parsed_t[JSONInputKeys.START_TIME] = cls._parse_dt(parsed_t[JSONInputKeys.START_TIME]).time()
                if parsed_t.get(JSONInputKeys.END_TIME):
                    parsed_t[JSONInputKeys.END_TIME] = cls._parse_dt(parsed_t[JSONInputKeys.END_TIME]).time()
                parsed_talks.append(FHTalk.from_dict(parsed_t))

            venue, venue_link = cls._parse_venue_details(data[JSONInputKeys.VENUE])

            return cls(
                session_number=data[JSONInputKeys.SESSION_NUMBER],
                date=parsed_date,
                venue=venue,
                venue_link=venue_link,
                no_hack=False,
                no_hack_reason=None,
                talks=parsed_talks,
                signup_link=data[JSONInputKeys.SIGNUP_LINK]
            )

    def to_schedule_ready_dict(self) -> Dict[str, Any]:
        """Convert the session details into a dictionary format ready for schedule update."""
        if self.no_hack:
            return {YAMLScheduleKeys.NOHACK: self.no_hack_reason or "No hack"}
        else:
            return {
                SessionOutputFields.VENUE: f'<a href="{self.venue_link}">{self.venue}</a>',
                SessionOutputFields.BLOG_POST: f"/{self.date.year}/{self.date.month:02d}/friday-hacks-{self.session_number}",
                SessionOutputFields.TOPICS: [talk.to_schedule_ready_dict() for talk in self.talks]
            }

    def __str__(self) -> str:
        """Return a human-readable string representation of the session."""
        talks_summary = f"{len(self.talks)} talk(s)" if self.talks else "no talks"
        if self.no_hack:
            return f"FHSession(#{self.session_number}, {self.date} NO HACK: {self.no_hack_reason})"
        return f"FHSession(#{self.session_number}, {self.date}, {self.venue}, {talks_summary})"

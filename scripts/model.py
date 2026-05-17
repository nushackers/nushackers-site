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
            YAMLScheduleKeys.START_DATE.value: self.start_date.strftime("%Y-%m-%d") + " 19:00:00 +0800",
            YAMLScheduleKeys.START_NR.value: self.start_nr,
            YAMLScheduleKeys.HACKS.value: self.hacks
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
        
        If week_number exceeds the current schedule length, extends self.hacks with 
        NOSPEAKER entries until the given week_number can be accommodated.

        Args:
            week_number: The week number to update (int)
            session_details: A dictionary containing the session details to update in the schedule
        """
        index = week_number - 1  # Convert 1-based week_number to 0-based index
        
        # Extend hacks array if necessary
        if index >= len(self.hacks):
            num_to_add = index - len(self.hacks) + 1
            for _ in range(num_to_add):
                self.hacks.append({YAMLScheduleKeys.NOSPEAKER.value: True})
        
        if 0 <= index < len(self.hacks):
            self.hacks[index] = session_details
        else:
            raise IndexError(f"Week number {week_number} is invalid. Must be >= 1.")


@dataclass
class FHTalk:
    """Represents a single talk at a Friday Hacks session."""
    speaker: str
    speaker_profile: str
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
        assert_fields_in_dictionary([TalkOutputFields.SPEAKER, TalkOutputFields.SPEAKER_PROFILE, TalkOutputFields.TITLE, TalkOutputFields.DESCRIPTION, TalkOutputFields.POSTER_LINK, JSONInputKeys.START_TIME, JSONInputKeys.END_TIME], data)

        return cls(
            speaker=data[TalkOutputFields.SPEAKER],
            speaker_profile=data[TalkOutputFields.SPEAKER_PROFILE],
            title=data[TalkOutputFields.TITLE],
            description=data[TalkOutputFields.DESCRIPTION],
            poster_link=data[TalkOutputFields.POSTER_LINK],
            talk_from=data.get(TalkOutputFields.TALK_FROM),
            start_time=data[JSONInputKeys.START_TIME],
            end_time=data[JSONInputKeys.END_TIME]
        )

    def to_schedule_ready_dict(self) -> Dict[str, Any]:
        d = {
            TalkOutputFields.SPEAKER.value: self.speaker,
            TalkOutputFields.TITLE.value: self.title,
        }
        if self.talk_from:
            d[TalkOutputFields.TALK_FROM.value] = self.talk_from
        return d

    def __str__(self) -> str:
        """Return a human-readable string representation of the talk."""
        from_str = f" (from {self.talk_from})" if self.talk_from else ""
        return f"FHTalk(speaker={self.speaker!r}, title={self.title!r}, time={self.start_time}-{self.end_time}{from_str})"


@dataclass
class FHSession:
    """Represents the details of a single Friday Hacks session."""
    session_number: int
    week_number: int
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
        # All sessions require week_number and date
        if JSONInputKeys.WEEK_NUMBER not in data:
            raise ValueError(f"Missing required field: '{JSONInputKeys.WEEK_NUMBER}'")
        if JSONInputKeys.DATE not in data:
            raise ValueError(f"Missing required field: '{JSONInputKeys.DATE}'")
        
        week_number = data[JSONInputKeys.WEEK_NUMBER]
        
        # Check if this is a no-hack session
        no_hack = data.get(JSONInputKeys.NO_HACK, False)

        if no_hack:
            # For no-hack sessions, only date and reason are required
            if not data.get(JSONInputKeys.NO_HACK_REASON):
                raise ValueError(f"{JSONInputKeys.NO_HACK} is True but {JSONInputKeys.NO_HACK_REASON} is missing or empty")

            parsed_date = cls._parse_dt(data[JSONInputKeys.DATE]).date()

            return cls(
                session_number=0,  # Placeholder for no-hack sessions
                week_number=week_number,
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
                week_number=week_number,
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
            return {YAMLScheduleKeys.NOHACK.value: self.no_hack_reason or "No hack"}
        else:
            return {
                SessionOutputFields.VENUE.value: f'<a href="{self.venue_link}">{self.venue}</a>',
                SessionOutputFields.BLOG_POST.value: f"/{self.date.year}/{self.date.month:02d}/friday-hacks-{self.session_number}",
                SessionOutputFields.TOPICS.value: [talk.to_schedule_ready_dict() for talk in self.talks]
            }

    def __str__(self) -> str:
        """Return a human-readable string representation of the session."""
        talks_summary = f"{len(self.talks)} talk(s)" if self.talks else "no talks"
        if self.no_hack:
            return f"FHSession(week #{self.week_number}, {self.date} NO HACK: {self.no_hack_reason})"
        return f"FHSession(#{self.session_number}, week #{self.week_number}, {self.date}, {self.venue}, {talks_summary})"

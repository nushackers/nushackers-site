import datetime
import re

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from constants import (
    KEY_HACKS, KEY_SESSION_NUMBER, KEY_DATE, KEY_START_DATE, KEY_START_NR, KEY_VENUE, KEY_NO_HACK, KEY_NO_HACK_REASON,
    KEY_TALKS, KEY_START_TIME, KEY_END_TIME, KEY_SIGNUP_LINK, SESSION_FIELD_BLOG_POST, SESSION_FIELD_TOPICS, SESSION_FIELD_VENUE,
    TALK_FIELD_SPEAKER, TALK_FIELD_TITLE, TALK_FIELD_DESCRIPTION, TALK_FIELD_POSTER_LINK, TALK_FIELD_FROM,
    SCHEDULE_FIELD_START_NR, SCHEDULE_FIELD_START_DATE, SCHEDULE_FIELD_HACKS
)


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
            KEY_START_DATE: self.start_date.strftime("%Y-%m-%d") + " 19:00:00 +0800",
            KEY_START_NR: self.start_nr,
            KEY_HACKS: self.hacks
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
        required_fields = [SCHEDULE_FIELD_START_NR, SCHEDULE_FIELD_START_DATE, SCHEDULE_FIELD_HACKS]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field for FHSchedule: '{field}'")

        # Parse start_date string (format: "YYYY-MM-DD HH:MM:SS +HHMM")
        start_date_str = data[SCHEDULE_FIELD_START_DATE]
        # Extract just the date part
        date_part = start_date_str.split()[0]
        start_date = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()

        return cls(
            start_nr=data[SCHEDULE_FIELD_START_NR],
            start_date=start_date,
            hacks=data[SCHEDULE_FIELD_HACKS]
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
        
        Raises:
            IndexError: If the calculated week number is out of range
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
        required_fields = [TALK_FIELD_SPEAKER, TALK_FIELD_TITLE, TALK_FIELD_DESCRIPTION, TALK_FIELD_POSTER_LINK, KEY_START_TIME, KEY_END_TIME]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field for FHTalk: '{field}'")

        return cls(
            speaker=data[TALK_FIELD_SPEAKER],
            title=data[TALK_FIELD_TITLE],
            description=data[TALK_FIELD_DESCRIPTION],
            poster_link=data[TALK_FIELD_POSTER_LINK],
            talk_from=data.get(TALK_FIELD_FROM),
            start_time=data[KEY_START_TIME],
            end_time=data[KEY_END_TIME]
        )

    def to_schedule_ready_dict(self) -> Dict[str, Any]:
        d = {
            TALK_FIELD_SPEAKER: self.speaker,
            TALK_FIELD_TITLE: self.title,
        }
        if self.talk_from:
            d[TALK_FIELD_FROM] = self.talk_from
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
        no_hack = data.get(KEY_NO_HACK, False)
        
        # All sessions require date
        if KEY_DATE not in data:
            raise ValueError(f"Missing required field: '{KEY_DATE}'")
        
        if no_hack:
            # For no-hack sessions, only date and reason are required
            if not data.get(KEY_NO_HACK_REASON):
                raise ValueError(f"{KEY_NO_HACK} is True but {KEY_NO_HACK_REASON} is missing or empty")
            
            parsed_date = cls._parse_dt(data[KEY_DATE]).date()
            
            return cls(
                session_number=0,  # Placeholder for no-hack sessions
                date=parsed_date,
                venue="",
                venue_link="",
                no_hack=True,
                no_hack_reason=data[KEY_NO_HACK_REASON],
                talks=[],
                signup_link=""
            )
        else:
            # For regular sessions, all fields are required
            required_fields = [KEY_SESSION_NUMBER, KEY_VENUE, KEY_TALKS, KEY_SIGNUP_LINK]
            for key in required_fields:
                if key not in data:
                    raise ValueError(f"Missing required field: '{key}'")
            
            if not data[KEY_TALKS]:
                raise ValueError(f"The '{KEY_TALKS}' field must be a non-empty list")
            
            parsed_date = cls._parse_dt(data[KEY_DATE]).date()
            
            parsed_talks = []
            for t in data[KEY_TALKS]:
                parsed_t = dict(t)
                if parsed_t.get(KEY_START_TIME):
                    parsed_t[KEY_START_TIME] = cls._parse_dt(parsed_t[KEY_START_TIME]).time()
                if parsed_t.get(KEY_END_TIME):
                    parsed_t[KEY_END_TIME] = cls._parse_dt(parsed_t[KEY_END_TIME]).time()
                parsed_talks.append(FHTalk.from_dict(parsed_t))
            
            venue, venue_link = cls._parse_venue_details(data[KEY_VENUE])
            
            return cls(
                session_number=data[KEY_SESSION_NUMBER],
                date=parsed_date,
                venue=venue,
                venue_link=venue_link,
                no_hack=False,
                no_hack_reason=None,
                talks=parsed_talks,
                signup_link=data[KEY_SIGNUP_LINK]
            )

    def to_schedule_ready_dict(self) -> Dict[str, Any]:
        """Convert the session details into a dictionary format ready for schedule update."""
        if self.no_hack:
            return {KEY_NO_HACK: self.no_hack_reason or "No hack"}
        else:
            return {
                KEY_VENUE: f'<a href="{self.venue_link}">{self.venue}</a>',
                SESSION_FIELD_BLOG_POST: f"/{self.date.year}/{self.date.month:02d}/friday-hacks-{self.session_number}",
                SESSION_FIELD_TOPICS: [talk.to_schedule_ready_dict() for talk in self.talks]
            }

    def __str__(self) -> str:
        """Return a human-readable string representation of the session."""
        talks_summary = f"{len(self.talks)} talk(s)" if self.talks else "no talks"
        if self.no_hack:
            return f"FHSession(#{self.session_number}, {self.date} NO HACK: {self.no_hack_reason})"
        return f"FHSession(#{self.session_number}, {self.date}, {self.venue}, {talks_summary})"

import datetime
import re

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from constants import (
    KEY_SESSION_NUMBER, KEY_DATE, KEY_VENUE, KEY_NO_HACK, KEY_NO_HACK_REASON,
    KEY_TALKS, KEY_START_TIME, KEY_END_TIME, KEY_SIGNUP_LINK,
    TALK_FIELD_SPEAKER, TALK_FIELD_TITLE, TALK_FIELD_DESCRIPTION, TALK_FIELD_POSTER_LINK, TALK_FIELD_FROM,
    SCHEDULE_FIELD_START_NR, SCHEDULE_FIELD_START_DATE, SCHEDULE_FIELD_HACKS
)


@dataclass
class FHSchedule:
    """Represents the Friday Hacks schedule for a semester."""
    start_nr: int
    start_date: datetime.date
    hacks: List[Dict[str, Any]]

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


@dataclass
class FHTalk:
    """Represents a single talk at a Friday Hacks session."""
    speaker: str
    title: str
    description: str
    poster_link: str
    talk_from: Optional[str] = None
    start_time: datetime.time
    end_time: datetime.time

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
        """Helper to parse JS ISO strings like 2026-05-14T10:00:00.000Z"""
        if not dt_str:
            return None
        return datetime.datetime.fromisoformat(dt_str.replace("Z", "+08:00"))

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
        for key in [KEY_SESSION_NUMBER, KEY_DATE, KEY_VENUE, KEY_TALKS, KEY_SIGNUP_LINK]:
            if key not in data:
                raise ValueError(f"Missing required field: '{key}'")

        if not data[KEY_TALKS]:
            raise ValueError(f"The '{KEY_TALKS}' field must be a non-empty list")

        no_hack = data.get(KEY_NO_HACK, False)
        if no_hack:
            if not data.get(KEY_NO_HACK_REASON):
                raise ValueError(f"{KEY_NO_HACK} is True but {KEY_NO_HACK_REASON} is missing or empty")

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
            no_hack=no_hack,
            no_hack_reason=data.get(KEY_NO_HACK_REASON),
            talks=parsed_talks,
            signup_link=data[KEY_SIGNUP_LINK]
        )

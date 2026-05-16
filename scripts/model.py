import datetime
import re

from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from constants import (
    KEY_SESSION_NUMBER, KEY_DATE, KEY_VENUE, KEY_NO_HACK, KEY_NO_HACK_REASON,
    KEY_TALKS, KEY_START_TIME, KEY_END_TIME, KEY_SIGNUP_LINK
)

@dataclass
class FHSession:
    session_number: int
    date: datetime.date
    venue: str
    venue_link: str
    no_hack: bool
    no_hack_reason: str | None
    talks: List[Dict[str, Any]]
    signup_link: str

    @classmethod
    def _parse_dt(cls, dt_str: str) -> datetime.datetime:
        """Helper to parse JS ISO strings like 2026-05-14T10:00:00.000Z"""
        if not dt_str:
            return None
        return datetime.datetime.fromisoformat(dt_str.replace("Z", "+00:00"))

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
            parsed_talks.append(parsed_t)

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

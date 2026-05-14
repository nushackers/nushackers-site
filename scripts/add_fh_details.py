import argparse
import json
import re
import sys
import datetime
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

KEY_SESSION_NUMBER = "session_number"
KEY_DATE = "date"
KEY_VENUE = "venue"
KEY_NO_HACK = "no_hack"
KEY_NO_HACK_REASON = "no_hack_reason"
KEY_TALKS = "talks"
KEY_START_TIME = "start_time"
KEY_END_TIME = "end_time"

def _parse_dt(dt_str: str) -> datetime.datetime:
    """Helper to parse JS ISO strings like 2026-05-14T10:00:00.000Z"""
    if not dt_str:
        return None
    return datetime.datetime.fromisoformat(dt_str.replace("Z", "+00:00"))

@dataclass
class FHSession:
    session_number: int
    date: datetime.date
    venue: str
    venue_link: str
    no_hack: bool
    no_hack_reason: str | None
    talks: List[Dict[str, Any]]

    @classmethod
    def parse_venue_details(cls, venue_str: str) -> Tuple[str, str]:
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
        for key in [KEY_SESSION_NUMBER, KEY_DATE, KEY_VENUE, KEY_TALKS]:
            if key not in data:
                raise ValueError(f"Missing required field: '{key}'")

        if not data[KEY_TALKS]:
            raise ValueError(f"The '{KEY_TALKS}' field must be a non-empty list")

        no_hack = data.get(KEY_NO_HACK, False)
        if no_hack:
            if not data.get(KEY_NO_HACK_REASON):
                raise ValueError(f"{KEY_NO_HACK} is True but {KEY_NO_HACK_REASON} is missing or empty")

        parsed_date = _parse_dt(data[KEY_DATE]).date()

        parsed_talks = []
        for t in data[KEY_TALKS]:
            parsed_t = dict(t)
            if parsed_t.get(KEY_START_TIME):
                parsed_t[KEY_START_TIME] = _parse_dt(parsed_t[KEY_START_TIME]).time()
            if parsed_t.get(KEY_END_TIME):
                parsed_t[KEY_END_TIME] = _parse_dt(parsed_t[KEY_END_TIME]).time()
            parsed_talks.append(parsed_t)

        venue, venue_link = cls.parse_venue_details(data[KEY_VENUE])

        return cls(
            session_number=data[KEY_SESSION_NUMBER],
            date=parsed_date,
            venue=venue,
            venue_link=venue_link,
            no_hack=no_hack,
            no_hack_reason=data.get(KEY_NO_HACK_REASON),
            talks=parsed_talks
        )

def main() -> None:
    parser = argparse.ArgumentParser(description="Process FH details from stdin.")
    parser.add_argument("session_number", type=int, help="The session number (integer).")
    parser.add_argument("semester", type=str, help="The semester string, following the pattern XXXX_1 or XXXX_2 (e.g., 2627_1).")

    args: argparse.Namespace = parser.parse_args()

    # Validate semester format
    if not re.match(r"^\d{4}_[12]$", args.semester):
        print(f"Error: Invalid semester format '{args.semester}'. It must match \\d{{4}}_[12]", file=sys.stderr)
        sys.exit(1)

    # Read JSON string from standard input
    raw_json: str = sys.stdin.read()

    # Parse JSON string
    try:
        data_dict: Dict[str, Any] = json.loads(raw_json)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON from stdin. {e}\nContent was: {raw_json[:100]}...", file=sys.stderr)
        sys.exit(1)

    session_model: FHSession = FHSession.from_dict(data_dict)

    print(f"Successfully parsed input for Session {args.session_number}, Semester {args.semester}.")
    print(f"Model loaded: Session {session_model.session_number} with {len(session_model.talks)} talks.")

if __name__ == "__main__":
    main()

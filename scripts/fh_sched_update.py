import datetime
import yaml
from pathlib import Path
from typing import Any, Dict, List, Optional

from constants import (
    KEY_SESSION_NUMBER, KEY_DATE, KEY_VENUE, KEY_NO_HACK, KEY_NO_HACK_REASON,
    KEY_TALKS, KEY_START_TIME, KEY_END_TIME, KEY_START_DATE, KEY_START_NR,
    KEY_HACKS, KEY_NOSPEAKER, KEY_NOHACK
)

def _load_or_create_schedule(
    semester: str, 
    start_date: datetime.date, 
    start_nr: int
) -> Dict[str, Any]:
    """
    Load the schedule YAML file for a semester, or create it if it doesn't exist.

    If the file exists at data/friday_hacks/friday_hacks_{semester}.yml, it is loaded
    and returned. Otherwise, a new schedule is created from the template structure,
    written to the file path, and returned.

    Args:
        semester: The semester string (e.g., "2627_1")
        start_date: The date of the first session (datetime.date)
        start_nr: The session number of the first session (int)

    Returns:
        The loaded or created schedule as a dictionary
    """
    schedule_path = Path("data") / "friday_hacks" / f"friday_hacks_{semester}.yml"

    if schedule_path.exists():
        with open(schedule_path, 'r') as f:
            return yaml.safe_load(f) or {}

    # Create the schedule from template
    # Format: YYYY-MM-DD 19:00:00 +0800
    formatted_date = start_date.strftime("%Y-%m-%d") + " 19:00:00 +0800"

    schedule = {
        KEY_START_DATE: formatted_date,
        KEY_START_NR: start_nr,
        KEY_HACKS: [
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOHACK: "Recess Week"},
            {KEY_NOHACK: "Midterms"},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOSPEAKER: True},
            {KEY_NOHACK: "Reading Week"},
            {KEY_NOHACK: "Exam Week"},
        ]
    }

    # Create parent directories if needed
    schedule_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the schedule file
    with open(schedule_path, 'w') as f:
        yaml.dump(schedule, f, default_flow_style=False, sort_keys=False)

    return schedule


def _save_schedule(semester: str, schedule: Dict[str, Any]) -> None:
    """
    Save the schedule dictionary to the YAML file.

    Args:
        semester: The semester string (e.g., "2627_1")
        schedule: The schedule dictionary to save
    """
    schedule_path = Path("data") / "friday_hacks" / f"friday_hacks_{semester}.yml"
    
    with open(schedule_path, 'w') as f:
        yaml.dump(schedule, f, default_flow_style=False, sort_keys=False)


def update_schedule_session(
    semester: str,
    session_number: int,
    venue: str,
    venue_link: str,
    date: datetime.date,
    talks: List[Dict[str, Any]],
    no_hack: bool = False,
    reason: Optional[str] = None
) -> None:
    """
    Update the schedule entry for a given session.

    Updates the schedule file at data/friday_hacks/friday_hacks_{semester}.yml
    with the session details at the appropriate index.

    Args:
        semester: The semester string (e.g., "2627_1")
        session_number: The session number to update
        venue: The venue name
        venue_link: The link to the venue
        date: The date of the session (datetime.date)
        talks: List of talk detail dictionaries with speaker, title, and optional from
        no_hack: Whether this is a no-hack session (default False)
        reason: The reason for no-hack (required if no_hack is True)
    """
    # Load the schedule
    schedule = _load_or_create_schedule(semester, date, session_number)

    # Calculate the index in the hacks array
    start_nr = schedule.get(KEY_START_NR, 1)
    hack_index = session_number - start_nr

    # Validate index
    if hack_index < 0 or hack_index >= len(schedule.get(KEY_HACKS, [])):
        raise ValueError(f"Session {session_number} is out of bounds for schedule (start_nr={start_nr}, hacks length={len(schedule.get(KEY_HACKS, []))})")

    if no_hack:
        # Create no-hack entry
        schedule[KEY_HACKS][hack_index] = {KEY_NOHACK: reason or "No hack"}
    else:
        # Create venue link as HTML
        venue_html = f'<a href="{venue_link}">{venue}</a>'

        # Format blog post path as /YYYY/MM/friday-hacks-{session_number}
        year = date.year
        month = f"{date.month:02d}"
        blog_post = f"/{year}/{month}/friday-hacks-{session_number}"

        # Build topics array from talks
        topics = []
        for talk in talks:
            topic_entry = {
                "speaker": talk.get("speaker", ""),
                "title": talk.get("title", "")
            }
            # Add 'from' field if present and non-empty
            if (talk_from := talk.get("from")):
                topic_entry["from"] = talk_from
            topics.append(topic_entry)

        # Create the schedule entry
        schedule_entry = {
            "venue": venue_html,
            "blog_post": blog_post,
            "topics": topics
        }

        schedule[KEY_HACKS][hack_index] = schedule_entry

    # Write the updated schedule back to file
    _save_schedule(semester, schedule)

    print(f"Updated schedule entry for session {session_number} in {semester}")


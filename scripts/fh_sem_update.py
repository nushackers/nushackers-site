import datetime
import yaml
from pathlib import Path
from typing import Any, Dict

# Dictionary keys
KEY_SESSION_NUMBER = "session_number"
KEY_DATE = "date"
KEY_VENUE = "venue"
KEY_NO_HACK = "no_hack"
KEY_NO_HACK_REASON = "no_hack_reason"
KEY_TALKS = "talks"
KEY_START_TIME = "start_time"
KEY_END_TIME = "end_time"

# YAML schedule keys
KEY_START_DATE = "start_date"
KEY_START_NR = "start_nr"
KEY_HACKS = "hacks"
KEY_NOSPEAKER = "nospeaker"
KEY_NOHACK = "nohack"

def load_or_create_schedule(
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


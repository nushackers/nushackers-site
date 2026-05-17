import datetime
import yaml

from model import FHSchedule, FHSession
from constants import (
    FH_SCHEDULE_DIR, YAMLScheduleKeys
)


def _load_schedule(semester: str) -> FHSchedule:
    """
    Load an existing schedule YAML file as an FHSchedule instance.

    Args:
        semester: The semester string (e.g., "2627_1")

    Returns:
        The loaded schedule as an FHSchedule instance

    Raises:
        FileNotFoundError: If the schedule file doesn't exist
    """
    schedule_path = FH_SCHEDULE_DIR / f"friday_hacks_{semester}.yml"

    if not schedule_path.exists():
        raise FileNotFoundError(f"Schedule file not found: {schedule_path}")

    with open(schedule_path, 'r') as f:
        data = yaml.safe_load(f) or {}

    return FHSchedule.from_dict(data)


def _create_schedule(start_date: datetime.date, start_nr: int) -> FHSchedule:
    """
    Create a new schedule with template structure.

    Args:
        semester: The semester string (e.g., "2627_1")
        start_date: The date of the first session (datetime.date)
        start_nr: The session number of the first session (int)

    Returns:
        A new FHSchedule instance with template structure
    """
    # Format: YYYY-MM-DD 19:00:00 +0800
    formatted_date = start_date.strftime("%Y-%m-%d") + " 19:00:00 +0800"

    hacks = [
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOHACK: "Recess Week"},
        {YAMLScheduleKeys.NOHACK: "Midterms"},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOSPEAKER: True},
        {YAMLScheduleKeys.NOHACK: "Reading Week"},
        {YAMLScheduleKeys.NOHACK: "Exam Week"},
    ]

    schedule_dict = {
        YAMLScheduleKeys.START_DATE: formatted_date,
        YAMLScheduleKeys.START_NR: start_nr,
        YAMLScheduleKeys.HACKS: hacks
    }

    return FHSchedule.from_dict(schedule_dict)


def _load_or_create_schedule(
    semester: str, 
    start_date: datetime.date, 
    start_nr: int
) -> FHSchedule:
    """
    Load the schedule YAML file for a semester, or create it if it doesn't exist.

    If the file exists at data/friday_hacks/friday_hacks_{semester}.yml, it is loaded
    and returned as an FHSchedule instance. Otherwise, a new schedule is created from
    the template structure, written to the file path, and returned.

    Args:
        semester: The semester string (e.g., "2627_1")
        start_date: The date of the first session (datetime.date)
        start_nr: The session number of the first session (int)

    Returns:
        The loaded or created schedule as an FHSchedule instance
    """
    try:
        return _load_schedule(semester)
    except FileNotFoundError:
        schedule = _create_schedule(start_date, start_nr)
        _save_schedule(semester, schedule)
        return schedule


def _save_schedule(semester: str, schedule: FHSchedule) -> None:
    """
    Save the FHSchedule instance to the YAML file.

    Args:
        semester: The semester string (e.g., "2627_1")
        schedule: The FHSchedule instance to save
    """
    schedule_path = FH_SCHEDULE_DIR / f"friday_hacks_{semester}.yml"

    # Create parent directories if needed
    schedule_path.parent.mkdir(parents=True, exist_ok=True)

    with open(schedule_path, 'w') as f:
        yaml.dump(schedule.to_dict(), f, default_flow_style=False, sort_keys=False)


def update_schedule_session(start_nr: int, semester: str, session: FHSession) -> None:
    """
    Update the schedule entry for a given session using FHSession data.

    Updates the schedule file at data/friday_hacks/friday_hacks_{semester}.yml
    with the session details at the appropriate week_number index.

    Args:
        start_nr: The session number of the first session (int)
        semester: The semester string (e.g., "2627_1")
        session: The FHSession instance containing session details (includes week_number)
    """
    # Load or create schedule
    schedule = _load_or_create_schedule(semester, session.date, start_nr)

    # Update using the session's week number and ready-formatted data
    schedule.update_session(session.week_number, session.to_schedule_ready_dict())

    # Save the updated schedule
    _save_schedule(semester, schedule)

    print(f"Updated schedule entry for session {session.session_number} in {semester}")


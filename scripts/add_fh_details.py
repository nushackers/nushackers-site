import argparse
import json
import re
import sys
from typing import Any, Dict

from model import FHSession
from fh_sched_update import update_schedule_session
from fh_post_update import create_or_update_post

def main() -> None:
    parser = argparse.ArgumentParser(description="Process FH details from stdin.")
    parser.add_argument("start_nr", type=int, help="The first session number (integer).")
    parser.add_argument("semester", type=str, help="The semester string, following the pattern XXXX_1 or XXXX_2 (e.g., 2627_1).")
    parser.add_argument("start_date", type=str, help="The starting date for the semester in ISO format (e.g., 2026-04-05T19:00:00+0800).")

    args: argparse.Namespace = parser.parse_args()

    if not re.match(r"^\d{4}_[12]$", args.semester):
        print(f"Error: Invalid semester format '{args.semester}'. It must be in the format XXXX_1 or XXXX_2. (e.g., 2627_1, 2728_2)", file=sys.stderr)
        sys.exit(1)
    
    start_date = FHSession._parse_dt(args.start_date)
    if not start_date:
        print(f"Error: Invalid start date format '{args.start_date}'. It must be in ISO format (e.g., 2026-04-05T19:00:00+0800).", file=sys.stderr)
        sys.exit(1)

    raw_json: str = input()

    try:
        data_dict: Dict[str, Any] = json.loads(raw_json)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON from stdin. {e}\nContent was: {raw_json[:100]}...", file=sys.stderr)
        sys.exit(1)

    session_model: FHSession = FHSession.from_dict(data_dict)

    print(f"Successfully parsed input with start session {args.start_nr}, semester {args.semester}.")
    print(f"Model loaded: {session_model}")

    # Validate session model structure early before any file operations
    try:
        _ = session_model.to_schedule_ready_dict()
        print(f"Successfully validated session model structure.")
    except Exception as e:
        print(f"Error: Session model validation failed - {e}", file=sys.stderr)
        sys.exit(1)

    # Update the schedule file
    try:
        update_schedule_session(args.start_nr, args.semester, session_model, start_date)
    except Exception as e:
        print(f"Error: Failed to update schedule. {e}", file=sys.stderr)
        sys.exit(1)

    # Create or update the blog post
    try:
        create_or_update_post(session_model)
    except Exception as e:
        print(f"Error: Failed to create/update blog post. {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Successfully processed Friday Hacks session {session_model.session_number}!")

if __name__ == "__main__":
    main()

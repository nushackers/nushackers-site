import argparse
import json
import re
import sys
from typing import Any, Dict

from model import FHSession

def main() -> None:
    parser = argparse.ArgumentParser(description="Process FH details from stdin.")
    parser.add_argument("start_nr", type=int, help="The first session number (integer).")
    parser.add_argument("semester", type=str, help="The semester string, following the pattern XXXX_1 or XXXX_2 (e.g., 2627_1).")

    args: argparse.Namespace = parser.parse_args()

    if not re.match(r"^\d{4}_[12]$", args.semester):
        print(f"Error: Invalid semester format '{args.semester}'. It must match \\d{{4}}_[12]", file=sys.stderr)
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

if __name__ == "__main__":
    main()

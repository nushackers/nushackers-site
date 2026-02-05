#!/usr/bin/env python3

import argparse
import calendar
import os
import re
import sys
from typing import Any, Dict, Tuple


###############################
# Directories, template files #
###############################
FH_SCHED_DIR = os.path.join("data", "friday_hacks")
TEMPLATE_SEMESTER_FILE = os.path.join("scripts", "templates", "fh_semester_template.yml")


##################
# Regex patterns #
##################
DATE_PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
FH_SCHED_PATTERN = re.compile(r"^friday_hacks_(\d{2})(\d{2})_([12])\.yml$")


#####################
# Utility functions #
#####################
def validate_date(date_str: str) -> Tuple[str, str, str] | None:
    """Validate date format YYYY-MM-DD"""
    return DATE_PATTERN.match(date_str).groups() if DATE_PATTERN.match(date_str) else None

def replace_placeholders(template: str, replacements: Dict[str, Any]) -> str:
    """Replace placeholders in the template with actual values"""
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, str(value))
    return template


##################################
# FH semester schedule functions #
##################################
def get_latest_semester_info() -> str | None:
    """Find the latest semester file and calculate next semester info"""
    if not os.path.exists(FH_SCHED_DIR):
        print("Schedule directory not found: " + FH_SCHED_DIR, file=sys.stderr)
        return None

    files = sorted(
        [f for f in os.listdir(FH_SCHED_DIR) if FH_SCHED_PATTERN.match(f)],
        reverse=True
    )

    if not files:
        print("No semester files found in " + FH_SCHED_DIR, file=sys.stderr)
        return None

    latest_file = files[0]

    # extract acadyear and semester from filename "friday_hacks_<acadyear>_<semester>.yml"
    match = FH_SCHED_PATTERN.match(latest_file)

    acadyear1, acadyear2, semester = match.group(1), match.group(2), int(match.group(3))

    # acadyear is split into 2 parts: 2526 -> 25, 26
    # if semester = 1, then keep acadyear as is, and semester = 2
    # else if semester = 2, then acadyear -> (first part + 1)(second part + 1), semester = 1
    if semester == 1:
        next_acadyear = f"{acadyear1}{acadyear2}"
        next_semester = 2
    else:
        first_part = int(acadyear1) + 1
        second_part = int(acadyear2) + 1
        next_acadyear = f"{first_part}{second_part}"
        next_semester = 1

    return f"{next_acadyear}_{next_semester}"


def create_semester_schedule(start_date: str, start_nr: str) -> bool:
    """Create new semester schedule file"""
    # validate date format
    if not validate_date(start_date):
        print("Error: Invalid date format. Use YYYY-MM-DD")
        return False

    # validate that start_nr is a number
    if not start_nr.isdigit():
        print("Error: Start number must be a valid number")
        return False

    # check template file exists
    if not os.path.exists(TEMPLATE_SEMESTER_FILE):
        print(f"Error: Template file not found at {TEMPLATE_SEMESTER_FILE}")
        return False

    # get next semester info
    next_info = get_latest_semester_info()
    if not next_info:
        return False

    new_filename = os.path.join(FH_SCHED_DIR, f"friday_hacks_{next_info}.yml")

    if os.path.exists(new_filename):
        print(f"Error: File {new_filename} already exists")
        return False

    year, month, day = validate_date(start_date)

    # read template and replace placeholders
    with open(TEMPLATE_SEMESTER_FILE, "r") as f:
        template_content = f.read()

    template_content = replace_placeholders(template_content, {
        "YYYY": year,
        "MM": month,
        "DD": day,
        "XXX": start_nr
    })

    # write to new file
    with open(new_filename, "w") as f:
        f.write(template_content)

    print(f"Created new semester file: {new_filename}")
    return True

##############
# Main logic #
##############
def main():
    """Main logic"""
    parser = argparse.ArgumentParser(
        description="Generate a new Friday Hacks semester schedule file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Example:
  %(prog)s 2026-01-30 300"""
    )

    parser.add_argument(
        "date",
        help="Start date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "number",
        help="Starting Friday Hacks number"
    )

    args = parser.parse_args()

    success = create_semester_schedule(args.date, args.number)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

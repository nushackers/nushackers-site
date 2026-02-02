#!/usr/bin/env python3

import argparse
import calendar
import os
import sys
import re

# directories and template files
FH_POSTS_DIR = "content/post"
FH_SCHED_DIR = "data/friday_hacks"
TEMPLATE_SEMESTER_FILE = "scripts/templates/fh_semester_template.yml"
TEMPLATE_POST_FILE = "scripts/templates/fh_post_template.md"

# patterns
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FH_BLOG_POST_PATTERN = re.compile(r".*friday-hacks-(\d+)\.md$")
FH_SCHED_PATTERN = re.compile(r"friday_hacks_(\d+)_(\d+)\.yml")

#####################
# Utility functions #
#####################
def validate_date(date_str: str) -> bool:
    """Validate date format YYYY-MM-DD"""
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return pattern.match(date_str) is not None

def replace_placeholders(template: str, replacements: dict) -> str:
    """Replace placeholders in the template with actual values"""
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    return template

####################################
# Friday Hacks blog post functions #
####################################
def get_latest_fh_number() -> int | None:
    """Find the latest Friday Hacks post number"""
    if not os.path.exists(FH_POSTS_DIR):
        print("Posts directory not found: " + FH_POSTS_DIR, file=sys.stderr)
        return None

    return sorted(
        [int(FH_BLOG_POST_PATTERN.match(f).group(1)) for f in os.listdir(FH_POSTS_DIR)
         if FH_BLOG_POST_PATTERN.match(f)],
        reverse=True
    )[0]

def create_fh_post(date: str) -> bool:
    """Create new Friday Hacks post"""
    # validate date format
    if not validate_date(date):
        print("Error: Invalid date format. Use YYYY-MM-DD")
        return False

    # check template file exists
    if not os.path.exists(TEMPLATE_POST_FILE):
        print(f"Error: Template file not found at {TEMPLATE_POST_FILE}")
        return False

    # parse the date
    year, month, day = date.split("-")
    month_name = calendar.month_name[int(month)]

    # get the latest Friday Hacks number
    latest_num = get_latest_fh_number()
    if latest_num is None:
        print("Error: Could not determine the latest Friday Hacks number")
        return False

    new_num = latest_num + 1

    # create new file
    new_filename = os.path.join(FH_POSTS_DIR, f"{date}-friday-hacks-{new_num}.md")

    if os.path.exists(new_filename):
        print(f"Error: File {new_filename} already exists")
        return False

    # read template and replace placeholders
    with open(TEMPLATE_POST_FILE, "r") as f:
        template_content = f.read()

    template_content = replace_placeholders(template_content, {
        "YYYY": year,
        "MM": month,
        "DD": day,
        "XXX": str(new_num),
        "mmm": month_name
    })

    # write to new file
    with open(new_filename, "w") as f:
        f.write(template_content)

    print(f"Created new Friday Hacks post: {new_filename} (Friday Hacks #{new_num})")
    return True


##################################
# FH semester schedule functions #
##################################
def get_latest_semester_info() -> str | None:
    """Find the latest semester file and calculate next semester info"""
    if not os.path.exists(FH_SCHED_DIR):
        print("Schedule directory not found: " + FH_SCHED_DIR, file=sys.stderr)
        return None

    files = sorted(
        [f for f in os.listdir(FH_SCHED_DIR)
         if f.startswith("friday_hacks_") and f.endswith(".yml")],
        reverse=True
    )

    if not files:
        print("No semester files found in " + FH_SCHED_DIR, file=sys.stderr)
        return None

    latest_file = files[0]

    # extract acadyear and semester from filename "friday_hacks_<acadyear>_<semester>.yml"
    match = FH_SCHED_PATTERN.match(latest_file)

    if not match:
        print("Error: Could not parse semester file " + latest_file, file=sys.stderr)
        return None

    acadyear = match.group(1)
    semester = int(match.group(2))

    # acadyear is split into 2 parts: 2526 -> 25, 26
    # if semester = 1, then keep acadyear as is, and semester = 2
    # else if semester = 2, then acadyear -> (first part + 1)(second part + 1), semester = 1
    if semester == 1:
        next_acadyear = acadyear
        next_semester = 2
    else:
        first_part = int(acadyear[:2]) + 1
        second_part = int(acadyear[2:]) + 1
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

    year, month, day = start_date.split("-")

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
        description="Generate new Friday Hacks posts and semester schedule files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s -semester 2026-01-30 300
  %(prog)s -fh 2025-02-10"""
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # FH semester schedule command
    semester_parser = subparsers.add_parser(
        "semester",
        help="Create a new semester schedule file"
    )
    semester_parser.add_argument(
        "date",
        help="Start date in YYYY-MM-DD format"
    )
    semester_parser.add_argument(
        "number",
        help="Starting Friday Hacks number"
    )

    # FH blog post command
    fh_parser = subparsers.add_parser(
        "fh",
        help="Create a new Friday Hacks post template"
    )
    fh_parser.add_argument(
        "date",
        help="Date in YYYY-MM-DD format"
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    if args.command == "semester":
        success = create_semester_schedule(args.date, args.number)
        sys.exit(0 if success else 1)

    elif args.command == "fh":
        success = create_fh_post(args.date)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

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
FH_POSTS_DIR = os.path.join("content", "posts")
FH_SCHED_DIR = os.path.join("data", "friday_hacks")
TEMPLATE_SEMESTER_FILE = os.path.join("scripts", "templates", "fh_semester_template.yml")
TEMPLATE_POST_FILE = os.path.join("scripts", "templates", "fh_post_template.md")


##################
# Regex patterns #
##################
DATE_PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
FH_BLOG_POST_PATTERN = re.compile(r"^.*friday-hacks-(\d+)\.md$")
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

####################################
# Friday Hacks blog post functions #
####################################
def get_latest_fh_number() -> int | None:
    """Find the latest Friday Hacks post number"""
    if not os.path.exists(FH_POSTS_DIR):
        print("Posts directory not found: " + FH_POSTS_DIR, file=sys.stderr)
        return None

    blog_posts = [f for f in os.listdir(FH_POSTS_DIR) if FH_BLOG_POST_PATTERN.match(f)]

    if not blog_posts:
        print("No Friday Hacks posts found in " + FH_POSTS_DIR, file=sys.stderr)
        return None

    return max(blog_posts)

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
    year, month, day = validate_date(date)
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
        "XXX": new_num,
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
        description="Generate new Friday Hacks posts and semester schedule files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s semester 2026-01-30 300
  %(prog)s fh 2025-02-06"""
    )

    parser.add_argument(
        "semester",
        nargs=2,
        metavar=("DATE", "NUM"),
        help="Create a new semester schedule file (requires DATE and NUM)"
    )
    parser.add_argument(
        "fh",
        metavar="DATE",
        help="Create a new Friday Hacks post template (requires DATE)"
    )

    args = parser.parse_args()

    if args.semester and args.fh:
        print("Error: Please specify only one of `semester` or `fh`", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    elif args.semester:
        success = create_semester_schedule(args.semester[0], args.semester[1])
        sys.exit(success)
    elif args.fh:
        success = create_fh_post(args.fh)
        sys.exit(success)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()

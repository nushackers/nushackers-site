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
TEMPLATE_POST_FILE = os.path.join("scripts", "templates", "fh_post_template.md")


##################
# Regex patterns #
##################
DATE_PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
FH_BLOG_POST_PATTERN = re.compile(r"^.*friday-hacks-(\d+)\.md$")


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


##############
# Main logic #
##############
def main():
    """Main logic"""
    parser = argparse.ArgumentParser(
        description="Generate a new Friday Hacks post",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Example:
  %(prog)s 2025-02-06"""
    )

    parser.add_argument(
        "date",
        help="Date in YYYY-MM-DD format"
    )

    args = parser.parse_args()

    success = create_fh_post(args.date)
    sys.exit(not success) # success == True -> exit code 0 else exit code 1


if __name__ == "__main__":
    main()

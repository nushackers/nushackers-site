#!/usr/bin/env python3

import argparse
import json
import os
import re
import sys
import yaml
from typing import Dict, Any, Optional

###############################
# Directories, template files #
###############################
FH_POSTS_DIR = os.path.join("content", "post")
FH_SCHED_DIR = os.path.join("data", "friday_hacks")

##################
# Regex patterns #
##################
def get_fh_blog_post_pattern(fhnum: str) -> re.Pattern:
    return re.compile(rf"^.*-friday-hacks-{fhnum}\.md$")

#####################
# Utility functions #
#####################
def find_post_file(fhnum: str) -> Optional[str]:
    """Find the blog post file for a given Friday Hacks number"""
    if not os.path.exists(FH_POSTS_DIR):
        print(f"Posts directory not found: {FH_POSTS_DIR}", file=sys.stderr)
        return None
    
    pattern = get_fh_blog_post_pattern(fhnum)
    for f in os.listdir(FH_POSTS_DIR):
        if pattern.match(f):
            return os.path.join(FH_POSTS_DIR, f)
            
    print(f"No blog post found for Friday Hacks #{fhnum}", file=sys.stderr)
    return None

def find_sched_file(acadyear: str) -> Optional[str]:
    """Find the semester schedule file for a given academic year"""
    sched_file = os.path.join(FH_SCHED_DIR, f"friday_hacks_{acadyear}.yml")
    if os.path.exists(sched_file):
        return sched_file
        
    sched_file_alt = os.path.join(FH_SCHED_DIR, f"friday_hacks_{acadyear}.yaml")
    if os.path.exists(sched_file_alt):
        return sched_file_alt
        
    print(f"Schedule file not found: {sched_file} or {sched_file_alt}", file=sys.stderr)
    return None


def sanitize_venue_name(venue: str) -> str:
    """Sanitize venue name to match keys in venue_map.json"""
    return "_".join(venue.strip().upper().split())

def get_venue_details(venue: str) -> Dict[str, Any]:
    """Get venue details based on venue name"""
    sanitized_venue_name = sanitize_venue_name(venue)
    with open(os.path.join(os.path.dirname(__file__), "venue_map.json"), "r") as f:
        venue_map = json.load(f)
    return venue_map.get(sanitized_venue_name, {})


####################################
# Friday Hacks update functions #
####################################
def update_fh_details(fhnum: str, acadyear: str) -> bool:
    """Prompt user for Friday Hacks details and update files"""
    post_file = find_post_file(fhnum)
    if not post_file:
        return False
        
    sched_file = find_sched_file(acadyear)
    if not sched_file:
        return False

    print(f"Found post file: {post_file}")
    print(f"Found schedule file: {sched_file}")
    
    venue = input("venue: ")
    speaker_1_name = input("speaker 1 name: ")
    talk_1_title = input("talk 1 title: ")
    talk_1_desc = input("talk 1 description: ")
    speaker_2_name = input("speaker 2 name: ")
    talk_2_title = input("talk 2 title: ")
    talk_2_desc = input("talk 2 description: ")

    venue_details = get_venue_details(venue)
    if not venue_details:
        print(f"Warning: Venue '{venue}' not found in venue_map.json. Venue details will be empty.", file=sys.stderr)
        venue_details = {
            "name": venue,
            "address": "",
            "link": ""
        }



    # TODO: In the future, this is where we would update the files directly
    # with the input variables using yaml and markdown parsing/replacement.

    return True

##############
# Main logic #
##############
def main():
    """Main logic"""
    parser = argparse.ArgumentParser(
        description="Update Friday Hacks details given the FH post number and academic year semester.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Example:
  %(prog)s 287 2526_2"""
    )

    parser.add_argument(
        "fhnum",
        help="Friday Hacks number (e.g., 235)"
    )
    
    parser.add_argument(
        "acadyear",
        help="Academic year and semester (e.g., 2526_1)"
    )

    args = parser.parse_args()

    success = update_fh_details(args.fhnum, args.acadyear)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
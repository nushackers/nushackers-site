#!/usr/bin/env python3

import os
import sys
import re

# directories and template files
FH_POSTS_DIR = "content/post"
FH_SCHED_DIR = "data/friday_hacks"
TEMPLATE_SEMESTER_FILE = "scripts/templates/fh_semester_template.yml"
TEMPLATE_POST_FILE = "scripts/templates/fh_post_template.md"

def usage():
    """Print usage information"""
    print("""Usage: {command} [OPTIONS]

Options:
    -semester DATE NUMBER     Create a new semester schedule file
                            DATE format: YYYY-MM-DD
                            NUMBER: starting Friday Hacks number

    -fh DATE                  Create a new Friday Hacks post template
                            DATE format: YYYY-MM-DD
  
Examples:
    {command} -semester 2026-01-30 300
    {command} -fh 2025-02-10
""".format(command=sys.argv[0]))

def get_latest_fh_number():
    """Find the latest Friday Hacks post number"""
    if not os.path.exists(FH_POSTS_DIR):
        return None
    
    max_num = 0
    pattern = re.compile(r".*friday-hacks-(\d+)\.md$")
    
    for filename in os.listdir(FH_POSTS_DIR):
        if "friday-hacks-" in filename and filename.endswith(".md"):
            match = pattern.match(filename)
            if match:
                num = int(match.group(1))
                if num > max_num:
                    max_num = num
    
    return max_num if max_num > 0 else None

def get_latest_semester_info():
    """Find the latest semester file and calculate next semester info"""
    if not os.path.exists(FH_SCHED_DIR):
        print("Schedule directory not found: " + FH_SCHED_DIR, file=sys.stderr)
        return None
    
    # Get all semester files and sort them
    files = [f for f in os.listdir(FH_SCHED_DIR) 
             if f.startswith("friday_hacks_") and f.endswith(".yml")]
    files.sort()
    
    if not files:
        print("No semester files found in " + FH_SCHED_DIR, file=sys.stderr)
        return None
    
    latest_file = files[-1]
    
    # Extract acadyear and semester from filename "friday_hacks_<acadyear>_<semester>.yml"
    pattern = re.compile(r"friday_hacks_(\d+)_(\d+)\.yml")
    match = pattern.match(latest_file)
    
    if not match:
        print("Error: Could not parse semester file " + latest_file, file=sys.stderr)
        return None
    
    acadyear = match.group(1)
    semester = int(match.group(2))
    
    # Calculate next semester
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

def validate_date(date_str: str) -> bool:
    """Validate date format YYYY-MM-DD"""
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return pattern.match(date_str) is not None

def month_to_name(month: str) -> str:
    """Convert month number to full month name"""
    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return months.get(int(month), "Invalid")

def create_semester(start_date: str, start_nr: str) -> bool:
    """Create new semester file"""
    # Validate arguments
    if not start_date or not start_nr:
        print("Error: -semester requires DATE and NUMBER arguments")
        usage()
        return False
    
    # Validate date format
    if not validate_date(start_date):
        print("Error: Invalid date format. Use YYYY-MM-DD")
        return False
    
    # Validate that start_nr is a number
    if not start_nr.isdigit():
        print("Error: Start number must be a valid number")
        return False
    
    # Check template file exists
    if not os.path.exists(TEMPLATE_SEMESTER_FILE):
        print(f"Error: Template file not found at {TEMPLATE_SEMESTER_FILE}")
        return False
    
    # Get next semester info
    next_info = get_latest_semester_info()
    if not next_info:
        return False
    
    new_filename = os.path.join(FH_SCHED_DIR, f"friday_hacks_{next_info}.yml")
    
    if os.path.exists(new_filename):
        print(f"Error: File {new_filename} already exists")
        return False
    
    # Parse the date
    year, month, day = start_date.split("-")
    
    # Read template and replace placeholders
    with open(TEMPLATE_SEMESTER_FILE, "r") as f:
        template_content = f.read()
    
    # Replace placeholders
    template_content = template_content.replace("YYYY", year)
    template_content = template_content.replace("MM", month)
    template_content = template_content.replace("DD", day)
    template_content = template_content.replace("XXX", start_nr)
    
    # Write to new file
    with open(new_filename, "w") as f:
        f.write(template_content)
    
    print(f"Created new semester file: {new_filename}")
    return True

def create_fh_post(date: str) -> bool:
    """Create new Friday Hacks post"""
    # Validate date format
    if not validate_date(date):
        print("Error: Invalid date format. Use YYYY-MM-DD")
        return False
    
    # Check template file exists
    if not os.path.exists(TEMPLATE_POST_FILE):
        print(f"Error: Template file not found at {TEMPLATE_POST_FILE}")
        return False
    
    # Parse the date
    year, month, day = date.split("-")
    month_name = month_to_name(month)
    
    # Get the latest Friday Hacks number
    latest_num = get_latest_fh_number()
    if latest_num is None:
        print("Error: Could not determine the latest Friday Hacks number")
        return False
    
    # Increment the number
    new_num = latest_num + 1
    
    # Create new filename
    new_filename = os.path.join(FH_POSTS_DIR, f"{date}-friday-hacks-{new_num}.md")
    
    if os.path.exists(new_filename):
        print(f"Error: File {new_filename} already exists")
        return False
    
    # Read template and replace placeholders
    with open(TEMPLATE_POST_FILE, "r") as f:
        template_content = f.read()
    
    # Replace placeholders
    template_content = template_content.replace("YYYY", year)
    template_content = template_content.replace("MM", month)
    template_content = template_content.replace("DD", day)
    template_content = template_content.replace("XXX", str(new_num))
    template_content = template_content.replace("mmm", month_name)
    
    # Write to new file
    with open(new_filename, "w") as f:
        f.write(template_content)
    
    print(f"Created new Friday Hacks post: {new_filename} (Friday Hacks #{new_num})")
    return True

def main():
    """Main logic"""
    if len(sys.argv) == 1:
        usage()
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "-h" or command == "--help":
        usage()
        sys.exit(0)
    
    elif command == "-semester":
        if len(sys.argv) < 4:
            print("Error: -semester requires DATE and NUMBER arguments")
            usage()
            sys.exit(1)
        success = create_semester(sys.argv[2], sys.argv[3])
        sys.exit(0 if success else 1)
    
    elif command == "-fh":
        if len(sys.argv) < 3:
            print("Error: -fh requires a date argument")
            usage()
            sys.exit(1)
        success = create_fh_post(sys.argv[2])
        sys.exit(0 if success else 1)
    
    else:
        print(f"Error: Unknown option \"{command}\"")
        usage()
        sys.exit(1)

if __name__ == "__main__":
    main()

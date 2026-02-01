#!/bin/bash

readonly FH_POSTS_DIR="content/post"
readonly FH_SCHED_DIR="data/friday_hacks"
readonly TEMPLATE_SEMESTER_FILE="scripts/templates/fh_semester_template.yml"
readonly TEMPLATE_POST_FILE="scripts/templates/fh_post_template.md"

# Print usage information
usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Options:
  -semester DATE NUMBER  Create a new semester schedule file
                         DATE format: YYYY-MM-DD
                         NUMBER: starting Friday Hacks number
  -fh DATE               Create a new Friday Hacks post template
                         DATE format: YYYY-MM-DD
  
Examples:
  $0 -semester 2026-01-30 300
  $0 -fh 2025-02-10
EOF
}

# Find the latest Friday Hacks post number
get_latest_fh_number() {
    # Find all friday-hacks-<number>.md files, extract the number, and get the max
    ls -1 "$FH_POSTS_DIR"/*friday-hacks-*.md 2>/dev/null | \
        sed -E 's/.*friday-hacks-([0-9]+)\.md/\1/' | \
        sort -n | \
        tail -1
}

# Find the latest semester file and get its info
get_latest_semester_info() {
    local latest_file
    latest_file=$(ls -1 "$FH_SCHED_DIR"/friday_hacks_*.yml 2>/dev/null | sort | tail -1)
    
    if [ -z "$latest_file" ]; then
        echo "No semester files found"
        return 1
    fi
    
    # Extract filename without path
    local filename
    filename=$(basename "$latest_file")
    
    # Extract acadyear and semester from filename "friday_hacks_<acadyear>_<semester>.yml"
    # Using sed to extract: friday_hacks_2526_1.yml -> 2526 1
    local acadyear semester
    acadyear=$(echo "$filename" | sed -E 's/friday_hacks_([0-9]+)_([0-9]+)\.yml/\1/')
    semester=$(echo "$filename" | sed -E 's/friday_hacks_([0-9]+)_([0-9]+)\.yml/\2/')
    
    # Validate extraction
    if [ -z "$acadyear" ] || [ -z "$semester" ] || [ "$acadyear" = "$filename" ]; then
        echo "Error: Could not parse semester file" >&2
        return 1
    fi

    # acadyear is split into 2 parts: 2526 -> 25, 26
    # if semester = 1, then keep acadyear as is, and semester = 2
    # else if semester = 2, then acadyear -> (first part + 1)(second part + 1), semester = 1
    if [ "$semester" -eq 1 ]; then
        next_acadyear="$acadyear"
        next_semester=2
    else
        first_part=$((${acadyear%??} + 1))
        second_part=$((${acadyear#??} + 1))
        next_acadyear="${first_part}${second_part}"
        next_semester=1
    fi
    # return values
    echo "${next_acadyear}_${next_semester}"
}

# Create new semester file
create_semester() {
    local start_date="$1"
    local start_nr="$2"
    
    # Validate arguments
    if [ -z "$start_date" ] || [ -z "$start_nr" ]; then
        echo "Error: -semester requires DATE and NUMBER arguments"
        usage
        return 1
    fi
    
    # Validate date format
    if ! echo "$start_date" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'; then
        echo "Error: Invalid date format. Use YYYY-MM-DD"
        return 1
    fi
    
    # Validate that start_nr is a number
    if ! echo "$start_nr" | grep -qE '^[0-9]+$'; then
        echo "Error: Start number must be a valid number"
        return 1
    fi
    
    if [ ! -f "$TEMPLATE_SEMESTER_FILE" ]; then
        echo "Error: Template file not found at $TEMPLATE_SEMESTER_FILE"
        return 1
    fi
    
    next_info=$(get_latest_semester_info)
    
    if [ $? -ne 0 ]; then
        return 1
    fi

    local new_filename="$FH_SCHED_DIR/friday_hacks_${next_info}.yml"

    if [ -f "$new_filename" ]; then
        echo "Error: File $new_filename already exists"
        return 1
    fi

    # Parse the date
    local year="${start_date%%-*}"
    local month_day="${start_date#*-}"
    local month="${month_day%%-*}"
    local day="${month_day##*-}"
    
    # Read template and replace placeholders
    local template_content
    template_content=$(cat "$TEMPLATE_SEMESTER_FILE")
    
    # Replace placeholders (using sed for portability)
    template_content=$(echo "$template_content" | sed "s/YYYY/$year/g")
    template_content=$(echo "$template_content" | sed "s/MM/$month/g")
    template_content=$(echo "$template_content" | sed "s/DD/$day/g")
    template_content=$(echo "$template_content" | sed "s/XXX/$start_nr/g")
    
    # Write to new file
    echo "$template_content" > "$new_filename"
    echo "Created new semester file: $new_filename"
}

# Convert month number to full month name
month_to_name() {
    local month=$1
    # Remove leading zero to avoid octal interpretation
    month=$((10#$month))
    case $month in
        1) echo "January" ;;
        2) echo "February" ;;
        3) echo "March" ;;
        4) echo "April" ;;
        5) echo "May" ;;
        6) echo "June" ;;
        7) echo "July" ;;
        8) echo "August" ;;
        9) echo "September" ;;
        10) echo "October" ;;
        11) echo "November" ;;
        12) echo "December" ;;
        *) echo "Invalid" ;;
    esac
}

# Create new Friday Hacks post
create_fh_post() {
    local date="$1"
    
    # Validate date format YYYY-MM-DD
    if ! echo "$date" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'; then
        echo "Error: Invalid date format. Use YYYY-MM-DD"
        return 1
    fi
    
    if [ ! -f "$TEMPLATE_POST_FILE" ]; then
        echo "Error: Template file not found at $TEMPLATE_POST_FILE"
        return 1
    fi
    
    # Parse the date
    local year="${date%%-*}"
    local month_day="${date#*-}"
    local month="${month_day%%-*}"
    local day="${month_day##*-}"
    local month_name
    month_name=$(month_to_name "$month")
    
    # Get the latest Friday Hacks number
    local latest_num
    latest_num=$(get_latest_fh_number)
    
    if [ -z "$latest_num" ]; then
        echo "Error: Could not determine the latest Friday Hacks number"
        return 1
    fi
    
    # Increment the number
    local new_num=$((latest_num + 1))
    
    # Create new filename
    local new_filename="$FH_POSTS_DIR/${date}-friday-hacks-${new_num}.md"
    
    if [ -f "$new_filename" ]; then
        echo "Error: File $new_filename already exists"
        return 1
    fi
    
    # Read template and replace placeholders
    local template_content
    template_content=$(cat "$TEMPLATE_POST_FILE")
    
    # Replace placeholders (using sed for portability)
    template_content=$(echo "$template_content" | sed "s/YYYY/$year/g")
    template_content=$(echo "$template_content" | sed "s/MM/$month/g")
    template_content=$(echo "$template_content" | sed "s/DD/$day/g")
    template_content=$(echo "$template_content" | sed "s/XXX/$new_num/g")
    template_content=$(echo "$template_content" | sed "s/mmm/$month_name/g")
    
    # Write to new file
    echo "$template_content" > "$new_filename"
    echo "Created new Friday Hacks post: $new_filename (Friday Hacks #$new_num)"
}

# Main logic
if [ $# -eq 0 ]; then
    usage
    exit 0
fi

case "$1" in
    -semester)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Error: -semester requires DATE and NUMBER arguments"
            usage
            exit 1
        fi
        create_semester "$2" "$3"
        ;;
    -fh)
        if [ -z "$2" ]; then
            echo "Error: -fh requires a date argument"
            usage
            exit 1
        fi
        create_fh_post "$2"
        ;;
    *)
        echo "Error: Unknown option '$1'"
        usage
        exit 1
        ;;
esac

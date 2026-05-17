# Our Scripts

## Friday Hacks Scripts

Scripts to generate new Friday Hacks posts and semester schedule files.

### Automated FH Details Update: [`./scripts/add_fh_details.py`](./add_fh_details.py)

#### Usage

**Command-line arguments:**
```bash
python add_fh_details.py <start_nr> <semester> <start_date>
```

- `start_nr`: The first Friday Hacks session number (integer)
- `semester`: Semester string in format `XXXX_1` or `XXXX_2` (e.g., `2627_1`)
- `start_date`: The starting date for the semester in ISO format (e.g., `2026-04-05T19:00:00+0800`)

**Input:** JSON formatted session data via stdin. Required fields:
- `session_number`: The session number (integer)
- `week_number`: The week number for scheduling (integer, used to update schedule directly)
- `date`: ISO format datetime
- `venue`: Venue name with optional markdown link format `[name](url)`
- `talks`: Array of talk objects
- `signup_link`: Sign-up link for the session
- `no_hack`: Boolean, if true creates a no-hack week entry
- `no_hack_reason`: Reason for no-hack week (required if `no_hack` is true)

**Example:**
```bash
echo '{"session_number": 250, "week_number": 3, "date": "2026-04-12T19:00:00+0800", ...}' | python add_fh_details.py 250 2627_1 '2026-04-05T19:00:00+0800'
```

#### Behaviour

**With talks:** Validates all required fields (session number, week number, date, venue, talks, signup link), then updates the schedule and creates/replaces the blog post.

**No-hack weeks:** Updates the schedule with the no-hack reason only. Week number is still required.

**Schedule file exists:** Loads the existing schedule and updates the entry at the week_number index provided in the JSON input.

**Schedule file doesn't exist:** Creates a new schedule file using the `start_date` parameter as the semester start, with 14 total weeks (including Recess Week, Midterms, Reading Week, and Exam Week placeholders).

**Blog post file:** Creates new blog post if it doesn't exist, or replaces it if it does. Skipped for no-hack sessions.

### GitHub Workflow: Update Friday Hacks ([`.github/workflows/fh_updater.yaml`](../.github/workflows/fh_updater.yaml))

#### Inputs

- `start_nr`: Starting session number for the semester (integer)
- `semester`: Semester code in format `XXXX_1` or `XXXX_2` (e.g., `2627_1`)
- `start_date`: The starting date for the semester in ISO format (e.g., `2026-04-05T19:00:00+0800`)
- `session_data`: Session data as JSON
- `branch_suffix`: Branch identifier (e.g., `session-250`)

#### How it works

1. Creates a new branch named `branch-fh-{branch_suffix}`
2. Pipes the JSON session data to `add_fh_details.py` with `start_nr`, `semester`, and `start_date` arguments
3. Commits changes to `data/` and `content/` directories
4. Pushes the branch and automatically creates a pull request with review guidance

#### Integration with Google Apps Script

The Google Apps Script (apps_script.js) automatically:
- Filters ready Friday Hacks sessions from the spreadsheet
- Includes `week_number`, `session_number`, and other required fields in the JSON
- Triggers this workflow with the session data, start_nr, semester, start_date, and a branch suffix
- Updates the spreadsheet status when complete

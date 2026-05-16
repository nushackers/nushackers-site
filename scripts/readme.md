# Our Scripts

## Friday Hacks Scripts

Scripts to generate new Friday Hacks posts and semester schedule files.

### Automated FH Details Update: [`./scripts/add_fh_details.py`](./add_fh_details.py)

#### Usage

**Command-line arguments:**
```bash
python add_fh_details.py <session_number> <semester>
```

- `session_number`: The Friday Hacks session number (integer)
- `semester`: Semester string in format `XXXX_1` or `XXXX_2` (e.g., `2627_1`)

**Input:** JSON formatted session data via stdin

**Example:**
```bash
echo '{"session_number": 250, "date": "2026-04-12T19:00:00.000Z", ...}' | python add_fh_details.py 250 2627_1
```

#### Behaviour

**With talks:** Validates all required fields (session number, date, venue, talks, signup link), then updates the schedule and creates/replaces the blog post.

**No-hack weeks:** Updates the schedule with the no-hack reason only.

**Schedule file exists:** Loads the existing schedule, updates the entry for the session date (calculated from start_nr offset), and saves the updated schedule.

**Schedule file doesn't exist:** Creates a new schedule file assuming the first session (start_nr) is in week 3 of the semester, with 14 total weeks (including Recess Week, Midterms, Reading Week, and Exam Week placeholders).

**Blog post file:** Creates new blog post if it doesn't exist, or replaces it if it does.

### GitHub Workflow: Update Friday Hacks ([`.github/workflows/fh_update.yaml`](../.github/workflows/fh_update.yaml))

#### Inputs

- `start_nr`: Starting session number for the semester (integer)
- `semester`: Semester code in format `XXXX_1` or `XXXX_2` (e.g., `2627_1`)
- `session_data`: Session data as **base64-encoded JSON** (handled by apps_script.js)
- `branch_suffix`: Branch identifier (e.g., `session-250`)

#### How it works

1. Creates a new branch named `branch-fh-{branch_suffix}`
2. Decodes the base64-encoded session_data and pipes it to `add_fh_details.py`
3. Commits changes to `data/` and `content/` directories
4. Pushes the branch and automatically creates a pull request with review guidance

#### Integration with Google Apps Script

The Google Apps Script (apps_script.js) automatically:
- Filters ready Friday Hacks sessions from the spreadsheet
- Base64-encodes the session data
- Triggers this workflow with the encoded data
- Updates the spreadsheet status when complete

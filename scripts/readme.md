# Our Scripts

## Friday Hacks Scripts

Scripts to generate new Friday Hacks posts and semester schedule files.

### Automated FH Details Update: [`./scripts/add_fh_details.py`](./add_fh_details.py)

#### Usage

**Command-line arguments:**
```bash
python add_fh_details.py <start_nr> <semester> <start_date>
```

- `start_nr`: The first Friday Hacks session number (e.g. `250`)
- `semester`: Semester string in format `XXXX_1` or `XXXX_2` (e.g., `2627_1`)
- `start_date`: The starting date for the semester in ISO format (e.g., `2026-04-05T19:00:00+0800`)

**Example:**
```bash
python add_fh_details.py 250 2627_1 '2026-04-05T19:00:00+0800'
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
2. Passes the JSON session data via the `FH_SESSION_DATA` environment variable to `add_fh_details.py` with `start_nr`, `semester`, and `start_date` arguments
3. Commits changes to `data/` and `content/` directories
4. Pushes the branch and automatically creates a pull request with review guidance

#### Integration with Google Apps Script

The Google Apps Script (apps_script.js) automatically:
- Filters ready Friday Hacks sessions from the spreadsheet
- Includes `week_number`, `session_number`, and other required fields in the JSON
- Triggers this workflow with the session data, start_nr, semester, start_date, and a branch suffix
- Updates the spreadsheet status when complete

**IMPORTANT**: To work, the Apps Script needs a valid GitHub fine-grained PAT configured:
```js
const GITHUB_PAT = "YOUR_GITHUB_PAT";
```

Follow the steps [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) to create a PAT. Configure the following:

* Repository access - scope it to this repo (`nushackers/nushackers-site`)
* Permissions - minimally give it the `actions` permission with `read` and `workflows` permissions with `write`

### Upcoming features

- [ ] A single PAT will be in use and stored in a file in the Google Drive, and loaded into the script
- [ ] Google drive links of posters can be added to load the poster images directly. For now, they will need to be added to the PR manually.
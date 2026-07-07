# Friday Hacks Scripts [`./scripts/add_fh_details.py`](./add_fh_details.py)

Script to generate new Friday Hacks posts and semester schedule files.

## Setup for FH team

Every semester:
1. Create a google sheet, and add a table to it. The table schema columns should follow the same schema as the sheet [here](). You can also simply make a copy of that same sheet.
2. Add an Apps Script to the sheet. Copy the code from [`scripts/apps_script.js`](./apps_script.js) into the new script.
    * Steps 1-2 can be skipped by duplicating last semester's sheet. The table and apps script are duplicated when a sheet is duplicated.
    * Steps 3-5 need to be redone every semester, since the script properties and triggers are NOT duplicated along with the sheet and script.
3. Modify the following constants at the top of the file:
    ```js
    // Change every semester
    const SEMESTER = "2627_1";
    const START_NR = 250;
    const START_DATE = "2026-04-05T19:00:00+0800";
    ```
4. From our bitwarden, get the GitHub PAT. It should be called something like `GitHub FH PAT`.
5. Copy the PAT and add it as a Script property (Apps Script > Settings > scroll down to script properties > Property: `GITHUB_PAT`, Value: <copied PAT>)
6. Add a trigger (Apps Script > Triggers > Add Trigger). Use the following details:
    * Choose which function to run: `main`
    * Choose which deployment should run: leave it as-is (`head`)
    * Select event source and Select event type: either run it daily, or on edit. Up to the team.
    * Failure notification settings: `Notify me immediately`
    * Save the trigger
7. Ready to go!

Long-term:
1. The PAT should be rotated. Either do this using an account with admin access, or ask someone with admin access to follow these steps to create the PAT.
2. See [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) on how to create a fine-grained PAT. When creating the fine-grained PAT, give it the following permissions:
    * Scope it to repository, choose `nushackers/nushackers-site`
    * Actions - read/write
    * Workfows - read/write
    * Expiry - 1 year / should cover 2 semesters
3. Add it to bitwarden. Don't add new credentials, just update the previous item.

Note: Do NOT update past semester schedule app script properties. Only use the new PAT for subsequent semesters.

### CLI Usage

Note: the data needs to be formatted as a JSON string and stored to ENV, so this approach is NOT recommended.

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

## Behaviour

**With talks:** Validates all required fields (session number, week number, date, venue, talks, signup link), then updates the schedule and creates/replaces the blog post.

**No-hack weeks:** Updates the schedule with the no-hack reason only. Week number is still required.

**Schedule file exists:** Loads the existing schedule and updates the entry at the week_number index provided in the JSON input.

**Schedule file doesn't exist:** Creates a new schedule file using the `start_date` parameter as the semester start, with 14 total weeks (including Recess Week, Midterms, Reading Week, and Exam Week placeholders).

**Blog post file:** Creates new blog post if it doesn't exist, or replaces it if it does. Skipped for no-hack sessions.

## GitHub Workflow: Update Friday Hacks ([`.github/workflows/fh_updater.yaml`](../.github/workflows/fh_updater.yaml))

### Inputs

- `start_nr`: Starting session number for the semester (integer)
- `semester`: Semester code in format `XXXX_1` or `XXXX_2` (e.g., `2627_1`)
- `start_date`: The starting date for the semester in ISO format (e.g., `2026-04-05T19:00:00+0800`)
- `session_data`: Session data as JSON
- `branch_suffix`: Branch identifier (e.g., `session-250`)

### How it works

1. Creates a new branch named `branch-fh-{branch_suffix}`
2. Passes the JSON session data via the `FH_SESSION_DATA` environment variable to `add_fh_details.py` with `start_nr`, `semester`, and `start_date` arguments
3. Commits changes to `data/` and `content/` directories
4. Pushes the branch and automatically creates a pull request with review guidance

### Integration with Google Apps Script

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

## Upcoming features

- [ ] A single PAT will be in use and stored in a file in the Google Drive, and loaded into the script
- [ ] Google drive links of posters can be added to load the poster images directly. For now, they will need to be added to the PR manually.
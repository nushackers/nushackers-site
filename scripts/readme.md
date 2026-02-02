# Our Scripts

## Friday Hacks: [`./scripts/new-fh.py`](./new-fh.py)

Script to generate new Friday Hacks posts and semester schedule files.

### Usage

#### Help
```bash
python ./scripts/new-fh.py -h
```

```bash
python ./scripts/new-fh.py semester -h
```

```bash
python ./scripts/new-fh.py fh -h
```

#### Generate new FH semester schedule
```bash
python ./scripts/new-fh.py semester <first-FH-date> <first-FH-number>
```

Example:
```bash
python ./scripts/new-fh.py semester 2026-01-30 287
```

#### Generate new FH blog post
```bash
python ./scripts/new-fh.py fh <fh-date>
```

Example:
```bash
python ./scripts/new-fh.py fh 2026-01-30
```

### How it works

Uses templates in the [`scripts/templates/`](./templates/) directory to generate these files.


- **Dates MUST be in `YYYY-MM-DD` format.**
- For creating new FH posts, it automatically determines the FH number based on the previous FH number (last file in the folder when sorted in ascending order).
- For creating new semester schedules, it automatically figures out the academic year and semester number from the previous one.
- The semester schedule generation assumes that the first FH starts in week 3, with recess week, week 7 and reading week skipped. Public holidays are not considered.
- The generated files are templates only, you will still need to copy the details over manually.
- There is also a bash version of this script: [`./scripts/new-fh.sh`](./new-fh.sh). **The Python version is preferred.**

### Notes

Meant to replace the old script `scripts/gen_fh.py` since it uses an older format of FH post and has dependencies.

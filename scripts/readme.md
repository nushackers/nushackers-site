# NUS Hackers Scripts

## Friday Hacks: [`./scripts/new-fh.sh`](./new-fh.sh)

Script to generate new Friday Hacks posts and semester schedule files.

### Usage

#### Help
```bash
./scripts/new-fh.sh -h
```

#### Generate new FH semester schedule
```bash
./scripts/new-fh.sh -semester <first-FH-date> <first-FH-number>
```

Example:
```bash
./scripts/new-fh.sh -semester 2026-01-30 287
```

#### Generate new FH blog post
```bash
./scripts/new-fh.sh -fh <fh-date>
```

Example:
```bash
./scripts/new-fh.sh -fh 2026-01-30
```

### How it works

Uses templates in the [`scripts/templates/`](./templates/) directory to generate these files.


- Dates MUST be in `YYYY-MM-DD` format.
- For creating new FH posts, it automatically determines the FH number based on the previous FH number (last file in the folder when sorted in ascending order).
- For creating new semester schedules, it automatically figures out the academic year and semester number from the previous one.
- The semester schedule generation assumes that the first FH starts in week 3, with recess week, week 7 and reading week skipped. Public holidays are not considered.
- The generated files are templates only, you will still need to copy the details over manually.

### Notes

Meant to replace the old script `scripts/gen_fh.py` since it uses an older format of FH post and has dependencies.

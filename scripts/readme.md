# Our Scripts

## Friday Hacks Scripts

Scripts to generate new Friday Hacks posts and semester schedule files.

### Generate new FH blog post: [`./scripts/new-fh-post.py`](./new-fh-post.py)

#### Usage

**Help:**
```bash
./scripts/new-fh-post.py -h
```

**Generate new FH blog post:**
```bash
./scripts/new-fh-post.py <fh-date>
```

Example:
```bash
./scripts/new-fh-post.py 2026-01-30
```

#### How it works

- Uses the template in [`scripts/templates/fh_post_template.md`](./templates/fh_post_template.md) to generate the post file.
- Automatically determines the FH number based on the previous FH number (last file in the folder when sorted in ascending order).
- The generated file is a template only, you will still need to copy the details over manually.

### Generate new FH semester schedule: [`./scripts/new-fh-sem.py`](./new-fh-sem.py)

#### Usage

**Help:**
```bash
./scripts/new-fh-sem.py -h
```

**Generate new FH semester schedule:**
```bash
./scripts/new-fh-sem.py <first-fh-date> <first-fh-number>
```

Example:
```bash
./scripts/new-fh-sem.py 2026-01-30 287
```

#### How it works

- Uses the template in [`scripts/templates/fh_semester_template.yml`](./templates/fh_semester_template.yml) to generate the schedule file.
- Automatically figures out the academic year and semester number from the previous one.
- The semester schedule generation assumes that the first FH starts in week 3, with recess week, week 7 and reading week skipped. Public holidays are not considered.
- The generated file is a template only, you will still need to copy the details over manually.

### General Notes

> [!WARNING]
> **Dates MUST be in `YYYY-MM-DD` format.**

- These scripts are meant to replace the old script `scripts/gen_fh.py` since it uses an older format of FH post and has dependencies.

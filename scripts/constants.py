# Dictionary/JSON keys
from pathlib import Path

# Repository root directory (parent of scripts folder)
REPO_ROOT = Path(__file__).parent.parent

# Dictionary/JSON keys
KEY_DATE = "date"
KEY_VENUE = "venue"
KEY_NO_HACK = "no_hack"
KEY_NO_HACK_REASON = "no_hack_reason"
KEY_TALKS = "talks"
KEY_START_TIME = "start_time"
KEY_END_TIME = "end_time"
KEY_SIGNUP_LINK = "signup_link"

# YAML schedule keys
KEY_START_DATE = "start_date"
KEY_START_NR = "start_nr"
KEY_HACKS = "hacks"
KEY_NOSPEAKER = "nospeaker"
KEY_NOHACK = "nohack"

# FHSession field keys
SESSION_FIELD_BLOG_POST = "blog_post"
SESSION_FIELD_VENUE = "venue"
SESSION_FIELD_TOPICS = "topics"

# FHTalk field keys
TALK_FIELD_SPEAKER = "speaker"
TALK_FIELD_TITLE = "title"
TALK_FIELD_DESCRIPTION = "description"
TALK_FIELD_POSTER_LINK = "poster"
TALK_FIELD_FROM = "from"

# FHSchedule field keys
SCHEDULE_FIELD_START_NR = "start_nr"
SCHEDULE_FIELD_START_DATE = "start_date"
SCHEDULE_FIELD_HACKS = "hacks"

# Dictionary/JSON keys
from enum import StrEnum
from pathlib import Path

# Repository root directory (parent of scripts folder)
REPO_ROOT = Path(__file__).parent.parent
FH_SCHEDULE_DIR = REPO_ROOT / "data" / "friday_hacks"
FH_POST_DIR = REPO_ROOT / "content" / "post"


class JSONInputKeys(StrEnum):
    """Input JSON keys for Friday Hacks session data"""
    SESSION_NUMBER = "session_number"
    DATE = "date"
    WEEK_NUMBER = "week_number"
    VENUE = "venue"
    NO_HACK = "no_hack"
    NO_HACK_REASON = "no_hack_reason"
    TALKS = "talks"
    START_TIME = "start_time"
    END_TIME = "end_time"
    SIGNUP_LINK = "signup_link"


class YAMLScheduleKeys(StrEnum):
    """YAML schedule file keys"""
    START_DATE = "start_date"
    START_NR = "start_nr"
    HACKS = "hacks"
    NOSPEAKER = "nospeaker"
    NOHACK = "nohack"


class SessionOutputFields(StrEnum):
    """Session-level output fields for schedule"""
    BLOG_POST = "blog_post"
    VENUE = "venue"
    TOPICS = "topics"


class TalkOutputFields(StrEnum):
    """Talk-level output fields for schedule"""
    SPEAKER = "speaker"
    SPEAKER_PROFILE = "speaker_profile"
    TITLE = "title"
    DESCRIPTION = "description"
    POSTER_LINK = "poster"
    TALK_FROM = "from"

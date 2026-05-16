import datetime
from typing import List
from time import localtime, strftime

from model import FHSession, FHTalk
from constants import REPO_ROOT

METADATA_TEMPLATE = """\
---
title: "Friday Hacks # {{ session_number }}, {{ month_name }} {{ day }}: ..."
date: {{ year }}-{{ month }}-{{ day }} {{ current_time }}
author: yourname
url: /{{ year }}/{{ month }}/friday-hacks-{{ session_number }}
categories:
  - Friday Hacks
summary: ""
---
"""

EVENT_DETAILS_TEMPLATE = """\
**Date/Time:** {{ month_name }} {{ day }} at 7:00pm SGT<br />
**Venue:** [{{ venue }}]({{ venue_link }}) <br />
**Sign-up Link:** [Sign-up here]({{ signup_link }})<br />

> **Food 🍕 and Drinks 🧋 will be served!**
"""

SINGLE_TALK_TEMPLATE = """\
<img src="/img/{{ year }}/fh/{{ session_number }}-{{ idx }}.jpeg" style="height: 70%; width: 70%;" alt="Friday Hacks #{{ session_number }} Poster {{ idx }}" /><br />

## {{ idx }}) {{ title }}
{{ description }}

#### Speaker Profile 🎙️
{{ speaker_profile }}

<br /><br />
"""

SEE_YOU_THERE_STR = "👋 See you there!"


def _format_metadata(session_number: int, date: datetime.date) -> str:
    """
    Format the metadata template with session number, date, and current time.

    Args:
        session_number: The session number
        date: The date of the event (datetime.date)

    Returns:
        Formatted metadata string
    """
    current_time = strftime("%H:%M:%S", localtime())

    month_name = date.strftime("%B")
    day = date.day
    year = date.year
    month = f"{date.month:02d}"

    template = METADATA_TEMPLATE
    template = template.replace("{{ session_number }}", str(session_number))
    template = template.replace("{{ month_name }}", month_name)
    template = template.replace("{{ day }}", str(day))
    template = template.replace("{{ year }}", str(year))
    template = template.replace("{{ month }}", month)
    template = template.replace("{{ current_time }}", current_time)

    return template


def _format_event_details(date_obj: datetime.date, venue: str, venue_link: str, signup_link: str) -> str:
    """
    Format the event details template with date, venue, and signup information.
    
    Args:
        date_obj: The date of the event (datetime.date)
        venue: The venue name
        venue_link: The link to the venue
        signup_link: The signup link
    
    Returns:
        Formatted event details string
    """
    month_name = date_obj.strftime("%B")
    day = date_obj.day

    template = EVENT_DETAILS_TEMPLATE
    template = template.replace("{{ month_name }}", month_name)
    template = template.replace("{{ day }}", str(day))
    template = template.replace("{{ venue }}", venue)
    template = template.replace("{{ venue_link }}", venue_link)
    template = template.replace("{{ signup_link }}", signup_link)

    return template


def _format_talks(talks: List[FHTalk], date_obj: datetime.date, session_number: int) -> str:
    """
    Format an array of FHTalk instances into the single talk template.
    
    Args:
        talks: List of FHTalk instances
        date_obj: The date of the event (datetime.date)
        session_number: The session number
    
    Returns:
        Formatted talks string with all talks joined by newlines
    """
    year = date_obj.year
    formatted_talks = []

    for idx, talk in enumerate(talks, start=1):
        template = SINGLE_TALK_TEMPLATE
        template = template.replace("{{ year }}", str(year))
        template = template.replace("{{ session_number }}", str(session_number))
        template = template.replace("{{ idx }}", str(idx))
        template = template.replace("{{ title }}", talk.title)
        template = template.replace("{{ description }}", talk.description)
        # Use speaker name as the speaker profile since FHTalk doesn't have a separate profile field
        template = template.replace("{{ speaker_profile }}", f"Speaker: {talk.speaker}")

        formatted_talks.append(template)

    return "\n".join(formatted_talks)


def _generate_post_content(metadata: str, event_details: str, talks_content: str) -> str:
    """
    Join all formatted strings into the complete post content.
    
    Args:
        metadata: Formatted metadata string
        event_details: Formatted event details string
        talks_content: Formatted talks content string
    
    Returns:
        Complete post content with all sections joined
    """
    return "\n".join([metadata, event_details, talks_content, SEE_YOU_THERE_STR])


def create_or_update_post(session: FHSession) -> None:
    """
    Create or update a Friday Hacks blog post markdown file from an FHSession instance.
    
    Creates or updates the file at content/post/YYYY-MM-DD-friday-hacks-{session_number}.md
    with the formatted blog post content.
    
    Skips blog post creation for no-hack sessions.
    
    Args:
        session: The FHSession instance containing all session details
    """
    # Skip creating blog post for no-hack sessions
    if session.no_hack:
        print(f"Skipping blog post creation for no-hack session {session.session_number}: {session.no_hack_reason}")
        return

    # Convert date to string for file path
    date_str = session.date.strftime("%Y-%m-%d")

    # Format all sections
    metadata = _format_metadata(session.session_number, session.date)
    event_details = _format_event_details(session.date, session.venue, session.venue_link, session.signup_link)
    talks_content = _format_talks(session.talks, session.date, session.session_number)

    # Generate complete post content
    post_content = _generate_post_content(metadata, event_details, talks_content)

    # Construct file path using REPO_ROOT with os-agnostic delimiters
    file_path = REPO_ROOT / "content" / "post" / f"{date_str}-friday-hacks-{session.session_number}.md"

    # Create parent directories if needed
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the content to the file
    with open(file_path, 'w') as f:
        f.write(post_content)

    print(f"Blog post updated at {file_path}")



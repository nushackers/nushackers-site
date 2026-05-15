import datetime
from typing import Any, Dict, List
from time import localtime, strftime

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


def format_metadata(session_number: int, date_str: str) -> str:
    """
    Format the metadata template with session number, date, and current time.

    Args:
        session_number: The session number
        date_str: Date string in format YYYY-MM-DD

    Returns:
        Formatted metadata string
    """
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    current_time = strftime("%H:%M:%S", localtime())

    month_name = date_obj.strftime("%B")
    day = date_obj.day
    year = date_obj.year
    month = f"{date_obj.month:02d}"

    template = METADATA_TEMPLATE
    template = template.replace("{{ session_number }}", str(session_number))
    template = template.replace("{{ month_name }}", month_name)
    template = template.replace("{{ day }}", str(day))
    template = template.replace("{{ year }}", str(year))
    template = template.replace("{{ month }}", month)
    template = template.replace("{{ current_time }}", current_time)

    return template


def format_event_details(date_obj: datetime.date, venue: str, venue_link: str, signup_link: str) -> str:
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


def format_talks(talks: List[Dict[str, Any]], date_obj: datetime.date, session_number: int) -> str:
    """
    Format an array of talk details into the single talk template.
    
    Args:
        talks: List of talk detail dictionaries
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
        template = template.replace("{{ title }}", talk.get("title", f"Talk {idx}"))
        template = template.replace("{{ description }}", talk.get("description", f"Description for talk {idx}"))
        template = template.replace("{{ speaker_profile }}", talk.get("speaker_profile", f"Speaker profile for talk {idx}"))
        
        formatted_talks.append(template)
    
    return "\n".join(formatted_talks)


def generate_post_content(metadata: str, event_details: str, talks_content: str) -> str:
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



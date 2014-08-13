# Generate this week's friday hack
# Please first update _data/friday_hacks.yml before
# running this shit bro
import yaml
from datetime import datetime, timedelta
from os import listdir
from os.path import isfile, join
import re

with open('../_data/friday_hacks.yml', 'r') as fin:
    doc = yaml.load(fin)
    start_date = datetime.strptime(doc['start_date'],
                               '%Y-%m-%d %H:%M:%S +0800')
    now = datetime.today()
    hacks = doc['hacks']
    cur = start_date
    next_hack = None
    next_date = None
    for hack in hacks:
        if cur > now:
            next_hack = hack
            next_date = cur
            break
    if not next_hack:
        print "Dude semester's over"
        quit()

    if not next_hack.get('topics'):
        print "Dude no hackz"
        quit()

    name = raw_input("Your name bro? ")

    # so future-proof it's sick
    fhre = re.compile(
        r'^20[0-9][0-9]-[01][0-9]-[0-3][0-9]-friday-hacks-([1-9][0-9]*)-[a-z]*-[0-9]+\.md$')

    num = 0
    # so.. tempted... to... use lazy evaluation
    for f in listdir('../_posts/'):
        result = fhre.search(f)
        if result:
            cur = int(result.group(1))
            if cur > num:
                num = cur
    
    num += 1
    # now witness templating in raw string
    content = '''\
---
layout: friday_hack
title: "Friday Hacks #{num}, {month} {day}"
date: {now}
author: {author}
---

--- say something as introduction ---

{{% capture venue %}}
    {{{{ '{venue}' }}}}
{{% endcapture %}}
{{% include friday_hack_header.html %}}

'''.format(num=num,
           now=datetime.today(),
           month=next_date.strftime("%B"),
           day=next_date.day,
           author=name,
           venue=next_hack['venue']) + '\n'.join(['''
### {talk_name}

#### Talk Description:

--- describe ----

#### Speaker Profile

--- describe ----

'''.format(talk_name=topic['title']) for topic in next_hack['topics']])

    filename = '../_posts/{now}-friday-hacks-{num}-{month}-{day}.md'.format(
        now=next_date.strftime("%Y-%m-%d"),
        num=num,
        month=next_date.strftime('%b'),
        day=next_date.day,
    )

    with open(filename, 'a') as fout:
        fout.write(content)

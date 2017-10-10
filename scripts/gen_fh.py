# Generate this week's friday hack
# To generate some other FH pass in a number as argument
# e.g python gen_fh.py 1 generates next week's
# e.g python gen_fh.py 3 generates next next next week's
# Please first update data/friday_hacks.yml before running this
import yaml
from datetime import datetime, timedelta
from os import listdir
from os.path import isfile, join
from sys import argv
import re

with open('../data/friday_hacks.yml', 'r') as fin:
    doc = yaml.load(fin)
    start_date = datetime.strptime(doc['start_date'],
                               '%Y-%m-%d %H:%M:%S +0800')
    # Time delta fixes weird bug
    now = datetime.today() - timedelta(hours=3)

    # Sick undocumented feature
    if len(argv) > 1:
        now += timedelta(days = 7 * argv[1])

    hacks = doc['hacks']
    cur = start_date
    next_hack = None
    next_date = None
    for hack in hacks:
        if cur > now:
            next_hack = hack
            next_date = cur
            break
        cur += timedelta(days=7)
    if not next_hack:
        print "Dude semester's over"
        quit()

    if not next_hack.get('topics'):
        print "Dude no hackz"
        quit()

    name = raw_input("Your name? ")

    # so future-proof it's sick
    fhre = re.compile(
        r'^20[0-9][0-9]-[01][0-9]-[0-3][0-9]-friday-hacks-([1-9][0-9]*)-[a-zA-z]*-[0-9]+\.md$')

    num = 0
    # so.. tempted... to... use lazy evaluation
    for f in listdir('../content/post/'):
        result = fhre.search(f)
        if result:
            cur = int(result.group(1))
            if cur > num:
                num = cur

    num += 1
    # now witness templating in raw string
    content = '''\
---
title: "Friday Hacks #{num}, {month} {day}"
date: {now}
author: {author}
---

--- say something as introduction ---

{{{{% friday_hack_header venue="{venue}" date="{month} {day}" %}}}}

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

    filename = '../content/post/{now}-friday-hacks-{num}-{month}-{day}.md'.format(
        now=next_date.strftime("%Y-%m-%d"),
        num=num,
        month=next_date.strftime('%b'),
        day=next_date.day,
    )

    with open(filename, 'a') as fout:
        fout.write(content)

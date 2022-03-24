#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generate this week's friday hack
# To generate some other FH pass in a number as argument
# e.g python gen_fh.py 1 generates next week's
# e.g python gen_fh.py 3 generates next next next week's
# As for numbering, it will take the next number
# (e.g. if the previous post is FH #1000, the generated one will be FH #1001)
# Please first update data/friday_hacks.yml before running this
import yaml
from datetime import datetime, timedelta
from os import listdir
from os.path import isfile, join
from sys import argv
import re

with open('../data/friday_hacks.yml', 'r') as fin:
    doc = yaml.safe_load(fin)
    start_date = datetime.strptime(doc['start_date'],
                                   '%Y-%m-%d %H:%M:%S +0800')
    # Time delta fixes weird bug
    now = datetime.today() - timedelta(hours=3)

    # Sick undocumented feature
    if len(argv) > 1:
        now += timedelta(days=7 * int(argv[1]))

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
        print("Dude semester's over")
        quit()

    if not next_hack.get('topics'):
        print("Dude no hackz")
        quit()

    date = cur
    print("Creating FH post for " + str(cur))
    name = input("Your name? ")

    # so future-proof it's sick
    fhre = re.compile(
        r'^20[0-9][0-9]-[01][0-9]-[0-3][0-9]-friday-hacks-([1-9][0-9]*)\.md$')

    num = 0
    # so.. tempted... to... use lazy evaluation
    for f in listdir('../content/post/'):
        result = fhre.search(f)
        if result:
            cur = int(result.group(1))
            if cur > num:
                num = cur

    num += 1

    # In case you want to skip FH numbers BUT WHYYY!?!?
    # What is abstraction?
    # if len(argv) > 1:
    #     num += int(argv[1])

    print("Creating FH post for #" + str(num) + ", at " + str(date))
    # In case you want a different name, BUT WHYYY!?!?
    # name = raw_input("Your name? ")

    # now witness templating in raw string
    # nofh: true removes the Hangar footer which historically has supported us for Pizza, but no longer since Covid time
    content = '''\
---
title: "Friday Hacks #{num}, {month} {day}"
date: {now}
author: {author}
url: /{year}/{no_of_month}/friday-hacks-{num}
nofh: true
---

{{{{< friday_hack_header
    venue="{venue}"
    date="{year}-{no_of_month}-{day}T19:00:00+08:00"
    food="pizza"
    rsvp_link="#" >}}}}

'''.format(
        num=num,
        now=datetime.today(),
        year=next_date.strftime("%Y"),
        month=next_date.strftime("%B"),
        no_of_month=next_date.strftime('%m'),
        day=next_date.day,
        author=name,
        venue=next_hack['venue']) + '\n'.join([
            '''
## {number}) {talk_name}

--- describe ----

#### Speaker Profile

--- describe ----

'''.format(number=idx + 1, talk_name=topic['title']) for idx, topic in enumerate(next_hack['topics'])
        ])

    filename = '../content/post/{now}-friday-hacks-{num}.md'.format(
        now=next_date.strftime("%Y-%m-%d"),
        num=num,
        month=next_date.strftime('%b'),
        day=next_date.day,
    )

    with open(filename, 'a') as fout:
        fout.write(content)

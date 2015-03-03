---
layout: friday_hack
title: "Friday Hacks #89, March 6"
date: 2015-03-03 10:37:25
author: Jingwen
---

We're happy to have Haoyi, an engineer from Dropbox, speaking this week about the web
infrastructure at Dropbox. See 

{% capture venue %}
    {{ 'SR3, Town Plaza, UTown' }}
{% endcapture %}
{% include friday_hack_header.html %}

Facebook Event link: TBC

### Unruly Creatures: The Web Platform at Dropbox

#### Talk description

Making websites is hard; possibly harder than it should be. None of {HTML, CSS, JS, HTTP} are well designed or smooth developer experiences. It's even harder when you have over a hundred engineers of varying levels of experience and commitment, working on a 500kloc shared project, with legacy code going back to 2007, without even a compiler to help you catch mistakes!

This talk will cover the work we do on the Web Infrastructure team at Dropbox, about how we're using technology to help move the company forward. I'll cover the various ways in which we put code in your code to make the code that gets written better: abstraction, continuous integration and static analysis. Conventional and unconventional means that we use to move fast without breaking things.

#### Speaker profile

Haoyi is an engineer on the Web Infra and Developer Tools team who joined Dropbox after graduating in 2013. He likes functional programming and is the one person at Dropbox writing Scala full-time.

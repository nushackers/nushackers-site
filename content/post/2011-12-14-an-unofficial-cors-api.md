---
author: ejames
categories:
- Code
comments: true
date: 2011-12-14T00:00:00Z
title: An Unofficial CORS API
url: /2011/12/14/an-unofficial-cors-api/
---

We've happy to announce the release of an unofficial CORS API, available at <a href="http://api.nushackers.org/">api.nushackers.org</a>. Full usage details are available at <a href="http://api.nushackers.org">the API site</a>, but in sum, all API access is over HTTP, and is accessed from the api.nushackers.org domain. All data is received as JSON.

The project is open source and available on <a href="https://github.com/nushackers/cors-api">Github</a>. (The <a href="https://github.com/nushackers/cors-api/blob/master/readme.markdown">README</a> provides implementation details.) Ray Chuan will provide a requirements file in the near future. You'll need pymongo, MongoDB, Flask and Scrapy to run the project yourself,  but it's not a big project to read — just took 4 days to write — so do feel free to fork, comment, open bug reports, and send us Pull Requests.
<h3>Why?</h3>
There are two reasons for doing this: in the best case, we intend to ask the CORS team in NUS to implement a RESTful API (and we <strong>don't mind doing it for them</strong> - if anything, this project shows that the easy bit is the design and implementation of the API; the hard bit is in the scraping and parsing of data).

Should this approach fail, the NUS Hackers will host and maintain this API for as long as is needed.

The truth is, I think, that a CORS API is long overdue. Over the past few years, there have been a number of student-initiated projects to build better CORS-related tools. The Unofficial Timetable Builder, <a href="http://www.comp.nus.edu.sg/news/2010_Timetable_Builder2010.html">built originally</a> by Koh Zi Han, Tan Kian Boon, Liu Linxi and Wang Sha (and currently maintained by Zi Han), exposes a beautiful timetable-building interface to CORS. As does <a href="http://chrisirhc.github.com/nuschedule/">NUSchedule</a>, built originally by Lionel Chan, Victor Loh and Colin Tan (currently maintained by <a href="https://github.com/chrisirhc">Chris Chua</a>). Both project rely on scraping to get its timetable data; NUSchedule uses a clever <a href="https://github.com/chrisirhc/nuschedule/blob/master/js/Ripper.js">Javascript-based scraper</a>.

I'm not sure why the CORS team hasn't provided an API &mdash; Zi Han says that he's been petitioning for one for years. But I can guess as to the reasons: the CORS team may be overburdened, or perhaps they see little utility in building and maintaining an API.

Regardless, we'd love it if you build cool apps on top of this. You could build, say, a timetable builder, or a fast AJAXy search engine, or perhaps a Google Maps mashup to plot lecture and tutorial locations on a map of NUS!

We'll be in contact with the CORS team, and will update you as to the status of building an API for them. Hopefully, we'll not need to host this API for long.

Happy hacking!

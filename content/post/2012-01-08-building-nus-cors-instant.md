---
author: ejames
categories:
- Uncategorized
comments: true
date: 2012-01-08T00:00:00Z
title: Building NUS CORS Instant
url: /2012/01/08/building-nus-cors-instant/
---

<em>Rollen Gomes is a recently graduated NUS student. Here, he talks about the nuscors.com, an instant search for CORS built on top of the Unofficial CORS API.</em>

A couple weeks ago NUS Hackers released the unofficial NUS CORS API. I decided to leverage on the API to build something, just for the heck of it. Long story short I ended up building <a href="http://nuscors.com">nuscors.com</a>. The site is a faster way to search for a module in the NUS CORS database: you could call it an 'instant search'.

Now I’m gonna say this this a bluntly as possible, the initial design goals of the site were as follows. <span style="text-decoration: line-through;">Cheap</span> Free, Fast Search, Up before the CORS bidding period started. My other more sneaky goal was to have everyone in NUS use it and become a hero. Some of those goals were met and some are “in the pipeline”.

Anyway from this point on I speak some geek.

In the planning phase of the application and after some poking around I realised that the Unnoficial CORS API was written in Flask (Python). I immediately told myself to rewrite the API using some Ruby. Turns out the NUS CORS site was down on that day and life saved me from myself (phew). I ended up downloading the json file from the api site.

I used heroku as the hosting service for the application. This meant that the app was easy and free to deploy. Unfortunately, all free services come their limitations. In this case it was a 5 megabyte shared database. I didn’t want to have any connection with the database (pun intended) for a couple of reasons but most importantly it would add time to the page load.

In a nutshell the site works by downloading a static json file and then running a search on that downloaded file. Once the functionality was completed I designed the look and feel of the site to mimic Google instant search.

That, my friends, is how <a href="http://nuscors.com">nuscors.com</a> was born. Hope you enjoyed the read, if you have any questions join the <a href="https://groups.google.com/forum/?fromgroups#!forum/nushackers">NUS Hackers mailing list</a> and mail me there.

&nbsp;

---
author: ejames
categories:
- Code
comments: true
date: 2011-04-17T00:00:00Z
title: NUS-Specific Open Source Projects
url: /2011/04/17/nus-specific-open-source-projects-2/
---

One of the things we do at NUS Hackers is to encourage contributions to student-initiated open source projects. Sometimes we post links to such projects on the mailing list; other times we quietly fork the repository, contributing our own patches. Here are a couple of projects that we think deserve more love:
<blockquote><strong><a href="https://github.com/nushackers/printmonitor">SoC Print Monitor</a></strong> – is a program that monitors the print queue of all the NUS School of Computing network printers, and displays it on a <a href="http://www.comp.nus.edu.sg/~hirman/pm/">webpage</a>. It's one of the most insanely useful things I've found all year, and the people I've shown it to have grown used to having it around, as well.</blockquote>
<strong>Improvements</strong>: the program currently runs on Hirman (the creator)'s Sunfire account; according to a <a href="https://twitter.com/#!/bakavic">friend of mine</a>, it's leaking memory and restarts every once in awhile. A fix is recommended; also, last I checked — my friend Victor was hacking away on a program to print a document using drag-and-drop (to a browser), also based on Hirman's code.
<blockquote><strong><a href="https://github.com/chrisirhc/nuschedule">NUS Schedule</a></strong> — a jaw-dropping Javascript webapp that scrapes CORS, processes module data, and presents a AJAXified calendar interface for you to plan your NUS schedule. Try the webapp <a href="http://chrisirhc.github.com/nuschedule/">here</a>.</blockquote>
<strong>Improvements:</strong> the <a href="https://github.com/chrisirhc/nuschedule/issues">Github issues tab</a> indicates the following outstanding todos: i) iCal export, ii) gCal export, iii) a mobile version of the site and iv) module code autocompletion.
<blockquote><strong><a href="https://github.com/nushackers/IVLE-Forum-Leecher">IVLE Forum Leecher</a></strong> by Hong Dai Thanh — a Java program that scrapes the NUS IVLE forums and archives it on a user’s computer.</blockquote>
<strong>Improvements:</strong> Thanh confesses that he's unable to download the video lectures, because they're currently saved under Silverlight. A patch with a workaround would probably make him really happy.
<blockquote><a href="https://github.com/nushackers/NUS-Hackers-Theme"><strong>NUS Hackers.org WordPress Theme</strong></a> — a semantic, HTML5 theme currently in use on this very website. It's licensed under the GPL, and I use this theme as the basis for nearly all the school-related club sites I'm asked to do. Feel free to take it and do with it as you will.</blockquote>
We'd like to encourage all members to fork, contribute, or propose issues for any and all of these projects. The creators and/or maintainers will thank you for it. Also, do note that NUS Hackers operates a <a href="https://github.com/nushackers/">group repository</a> of its own on Github; if you currently own a NUS-centric open source project that you no longer have time to maintain, do contact us about it. We'll be more than willing to host it for you, and maintain it if need be.

You <em>should</em> be seeing some activity on the group repo this coming holidays. I know from speaking to the coreteam that a number of us are working on NUS-related personal projects: Angad's messing around with some filesharing code, Laurence will be leading the open source volunteer-platform for non-profits that we <a href="/2011/02/code-for-the-good-of-the-world/">intend to build</a>, and I'll be building a social news site to see if we can shift some things from Groups over to a webpage.

Happy hacking!

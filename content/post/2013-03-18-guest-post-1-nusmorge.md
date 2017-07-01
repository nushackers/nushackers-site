---
author: omer
categories:
- Uncategorized
comments: true
date: 2013-03-18T00:00:00Z
title: 'Guest Post #1 NUSMorge'
url: /2013/03/18/guest-post-1-nusmorge/
---

<em>In the spirit of hacking, we're starting a new series of posts exposing some of the projects made during the hack&amp;roll.</em> <a href="http://morge.nuscomputing.com/" target="_blank">NUSMorge</a><em> is a timetable merger, built on top of the Beng’s open source web app nusmods.com. It was built in 24 hours by team “Nange”, comprising of Yao Yujian, Wong Shen Nan, Joey Cheong and Ng Zhi An, who won “Best Freshman Effort” spot prize.</em>

<em> Here are some reflections by their team members:</em>
<h3>Yao Yujian</h3>
I had my 24-hour hackathon from this Sunday to Monday. Really great experience. Stayed up all night long coding non-stopped and produced something that actually works. Take a look at my <a href="https://github.com/yyjhao">github profile page</a> - there were 108 commits during that period! This is kind of funny because it is exactly half the number of commits I have pushed in a year.
Working in a team of four was also great. I don’t have to style the page, write up the server backend, or parse the data - all pushed to others :P.
Anyway, here’s the product we have hacked out: <a href="http://morge.nuscomputing.com/">NUSMorge</a>, a time table merger that takes in names and corresponding <a href="http://nusmods.com/">NUS mods</a> url and produce a merge of everyone’s time table so that you can clearly see all the free time slots. It even allows you to hide some of your lessons (for example, if you decide that you can skip that lecture, or that the lecturer has cancelled it) so you can maybe find more free time slots. For more information, please see <a href="http://yjyao.com/NUSMorge/">this introductory page</a>. It is also <a href="https://github.com/yyjhao/NUSMorge">open sourced</a>.
<h3>Ng Zhi An</h3>
<strong>What we built</strong>
Our team (Nange) built <a href="http://morge.nuscomputing.com/">NUSMorge</a> , a simple way for NUS students to visualize multiple time tables together. Check out our <a href="http://yjyao.com/NUSMorge/">intro page</a> too!
<strong>The Stack</strong>
NUSMorge is built on <a href="https://github.com/ngzhian/blog/blob/master/www.nodejs.org">Node.js</a> with <a href="https://github.com/ngzhian/blog/blob/master/www.expressjs.com">Express</a> serving our requests, <a href="http://www.mongodb.org/">mongoDB</a> taking care of unique links, with <a href="https://github.com/gett/mongojs">mongojs</a> as the glue. The rest of it (creating the table, merging the table, parsing the input url etc.) is Javascript, with help from <a href="http://jquery.com/">jQuery</a>.
NUSMorge also makes use of the json file crawled by <a href="http://nusmods.com/">NUSMods</a>. NUSMods is a timetable builder which many NUSStudents use. We take in a long url from NUSMods, and parse it into our own representation, and displays it in the our timetable.
<strong>Challenges</strong>
For most of us, hacking on something was a relatively new experience, what more having to work together as a team and come up with something at the end of 24 hours.
Communication is vital, stating clearly the route endpoints you expect to get, the object representation, error handling etc. All these were essential for your code to work together, and for the application to even work at all. It was hard to get the message across just by talking, so we drew and scribbled, and that really helped in our understanding.
Fatigue started to dawn upon us three quarters of the way through, but with the help of snacks and sugar, we managed to complete our application before some of us took a snooze.
Encouragement from each other helps a lot too!
<strong>Learning Points</strong>
Stay focused, stay motivated. 24 hours isn't a long time, to be able to ship something that works, it takes hard work. What is important is to get things working, then start adding features in if you have time.
Learn to distribute work, and learn the strengths of each member. Everyone will have an easier time this way.
Keep updating each other. Everyone should know what everyone else is working on this time. There needs to discussion and communication, so that members don't go working on the same thing (like writing two different ways of parsing), or working on wildly different things.
<strong>Source</strong>
Our <a href="https://github.com/yyjhao/NUSMorge">project</a> is on Github.

&nbsp;

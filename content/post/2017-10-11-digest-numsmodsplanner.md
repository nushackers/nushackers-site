---
author: Raynold Ng and Bay Wei Heng
categories:
  - Digest
date: 2017-10-11T00:00:00.000Z
title: >-
  Digest: How 2 inexperienced freshmen built an automated timetable generator
  over a summer
url: /2017/10/digest-nusmodsplanner/
aliases:
  - /2017/10/25/digest-nusmodsplanner/
---
# Introduction

Over the summer, we developed NUSMods Planner, an augmented version of NUSMods that comes with an automatic timetable planner. After much shameless marketing, it received much fanfare and user traffic. According to Google Analytics, we have about 2,600 users. Not bad for our first software project.

![](https://i.imgur.com/dIUcXfP.png)
*Snapshot of our Google Analytics Dashboard, taken in 27th September 2017*

![](https://i.imgur.com/WBm1NPGl.png)
*Screenshot of [NUSMods Planner](http://modsplanner.tk/), observe how the generated timetable has no lessons on Tuesday*


# How it all started

The same way every hack does: Over a casual chat with Wei Heng, we discovered we both found manual timetable planning too much of a chore.

There happened to be a school program (how to ahref this to nus orbital) sponsored by Google SG (tears we didnt get the Google trip) at that time, something like a summer-long hackathon, so "hey, why not".

# Features

Of course, our application would not have gotten so much attention if it merely prevented clashes given a fixed set of modules. Anyone can do that.

Features were actually implemented iteratively after various rounds of testing, by asking our peers what they would like to see in our app.

We had to make certain design decisions when considering whether to include X or Y in our final release, maintaining a balance between usability and usefulness. Allowing users overly fine-grained control usually meant more clutter in the UI, and we wanted a pleasant first-time user experience.

The final list of features are as follows (but why not check it out (at [NUSMods Planner](https://modsplanner.tk) yourself?):

- Optional Modules
- Workload Specification
- Locking lesson slots
- Free Days
- Lunch Hours
- Blocking out too early/late slots
- Website Tour

# First attempt at a solution

*(the more technically inclined may check out our [technical report](https://github.com/raynoldng/orbital-splashdown/blob/master/Splashdown_Technical_Report.pdf))*

After some research, we realised that since timetable planning can be expressed as a constraint problem, we could use powerful constraint solvers to help us. We started by learning about smtlibv2, what it could and could not achieve, and how long it would take to do so.

Then began the experimentation. For this part, we used [z3](https://github.com/Z3Prover/z3), a solver developed by Microsoft Research, which had exposed python api. We initially modeled the problem as an assignment of slots to hours, then used the Distinct API call to make sure there were no clashes. Even with no optional modules and no other constraints, results were dismal. One call took >3s on average, much slower than a naive recursive backtracking algorithm.

# What went wrong

The reason for this was that Distinct internally actually creates \\(n^2\\) (where $n$ is the total number of hours across all lessons in the specified modules) variables \\(a_i\neq a_j\\) and adds their conjunction to the constraint. The number of clauses was thus polynomially bigger than what we expected. We didn't want to give up on z3 and revert to the naive solution (recursive backtracking), since that would make supporting the features above impractical, so...


# Back to the drawing board

We had the Eureka moment while getting a drink at a cafe (did I mention we both love food): Instead of mapping lessons to hours, we could map each hour to a lesson (since timetables in NUS are fortnight-periodic)! Of course, there was still work to be done to properly express this concept in terms of first-order logic (we used selector variables and multiple implications), but once we did this, the solving time drastically improved. This method also could be naturally scaled to support all our intended features.

# We have a working, efficient algorithm, now what?

We met up with the NUSMods core team (Zhi An and Li Kai) for a demo, and they were impressed and agreed to be our mentors. They also tentatively agreed to code integration once we were done, subject to code quality. Over the course of the project, they provided invaluabe guidance and helped us navigate through their codebase, and we plan to finish codebase merging before their release of [NUSMods V3](https://v3.nusmods.com).

# Modifying the NUSMods codebase

Being total newbies to Web App development, this was a huge challenge, and in fact what we spent the most time on. We started by taking a [refresher course](https://learnxinyminutes.com/docs/javascript/) in JavaScript, then familiarising ourselves with [React](https://facebook.github.io/react/tutorial/tutorial.html) and [Redux](https://egghead.io/courses/getting-started-with-redux)

At first, we were confused as to why there was a need for so much boilerplate code, but as we implemented more and more features and bug-fixes, we were grateful that the codebase was so clean, structured and modular. Hot reloading and tools like [Redux DevTools](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=en) also made previewing changes a lot faster and debugging a lot easier.


# Pushing Work to the Client

Once we had written our timetable-generating scripts, we wrote a simple server app that would respond to queries by calling the scripts and then returning the results. We then deployed it on a Digital Ocean (DO) instance and benchmarked the response time using [Postman](https://www.getpostman.com/). To our horror, each query took the server **at least** 7 seconds to respond. Turns out our laptops were way more powerful than the DO instance (the cheapest option: 512 MB, we're both poor kids).

Clearly, doing the solving at the server side would not be scalable - there was no way NUSMods Planner could support the same user traffic as NUSMods unless we had access to some computing cluster.

We tried to improve the running time of the solving algorithm by optimizing the problem representation. While we managed to slash the average solving time by half, scalability remained an issue. We had no choice but to push the solving workload to the client.

So we had to find some way to run a SMT solver in the web browser. We came across the project called [ResearchJS](http://jgalenson.github.io/research.js/) that aims to share computer science research by compiling it to JavaScript. One of the shared research projects was [BoolectorJS](https://jgalenson.github.io/research.js/demos/boolector.html), a JavaScript version of [Boolector](http://fmv.jku.at/boolector/) compiled with [Emscripten](https://github.com/kripken/emscripten). The client would now load the BoolectorJS scripts and invoke them to solve our queries.

Here we would like to formally thank the above open-source project contributors - our project would not have been possible without them.

After three months of hardwork, this was how our full stack implementation looked like:

![](https://i.imgur.com/PeFL2oe.png)

# Further Work

Sadly our summer break was only 3 months; we were looking to add more features. One idea was to optimize the timetable based on some heuristic such as travelling distance or compactness of lessons. Solving optimization problems subject to constraints is an active research topic (see [here](https://link.springer.com/chapter/10.1007/978-3-642-29700-7_23)) but sadly not supported by most SMT solvers (we know that [z3 does](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/nbjorner-nuz.pdf)).

# Conclusion

As SMT solvers get more powerful and efficient, we can see SMT solvers being used as a catch-all solution for constraint-based problems. We look forward to more active development in JavaScript based SMT solvers and their application in web applications.

Overall we individually spent 200+ hours... It was heartwarming to have peers thanking us directly or providing postive [feedback](https://docs.google.com/forms/d/e/1FAIpQLScnDNgsB2K41EbWcDoMAyCmKRbwiB--Ih5t_E0r7Edf2VR_og/viewform) that they found the website useful.

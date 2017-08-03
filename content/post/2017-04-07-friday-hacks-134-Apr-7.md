---
author: Jethro Kuan
date: 2017-04-07T18:44:10Z
title: 'Friday Hacks #134, April 7'
url: /2017/04/07/friday-hacks-134-Apr-7/
---

Welcome back to our last episode of Friday Hacks for this semester! This week we'll be having Peter over to talk about Nix and NixOS. Nix and its related technologies bring a radically different approach to server/container management and allows you to provision OS and software in repeatable and consistent ways. Also, if you're curious about row hammering as a means of exploitation, mentioned last Friday Hacks by Halvar, Vishnu will be sharing about it in detail in the second talk.

{{% friday_hack_header venue="SR5, Town Plaza, University Town, NUS" date="April 7" %}}

### (Programming your OS && ignoring state) == bliss

#### Talk Description:
NixOS fundamentally changes how we approach servers, instances and infrastructure and it all comes down to a quirky functional programming language named "nix".

This talk covers some of the problems we can solve when we don't have to care about mutating state and how adding a real programming language to our infrastructure enables us to do things we couldn't do before.

#### Speaker Profile
Peter runs a small managed services company called Speartail, is CTO of a local SaaS startup and runs technical consulting company C2P4 with a partner where they help companies kick their tech stack and development processes into the next gear. He is also learning the violin much to his neighbors frustration.

He's @peterhoeg in most places online.

### Row Hammer: Flipping Bits in Memory Without Accessing Them

#### Talk Description:
“Row Hammer” is a problem with DRAM in which repeatedly accessing a row of memory can cause bit flips in adjacent rows. This talk will be describing how DRAM chips work, how the row hammer problem occured and finally how random bit flips in memory can be exploited into a privilege escalation attack.

#### Speaker Profile
Vishnu Prem is a senior Computer Science student in NUS who’s involved with the coreteam of NUS Hackers and the Singaporean tech scene. In the last few years, he has worked on software engineering projects for Twitter, Apple & Uber.

---
author: Ng Zhi An
categories:
- Digest
date: 2016-09-18T00:00:00Z
title: 'Digest: My experience interning at 3 companies'
url: /2016/09/18/digest-three-internships/
---

From Oct 2015 to Aug 2016, I had the good fortune of interning at 3 respectable companies: Google, Stripe, and Uber.

In this post I wish to share my experiences at the 3 different places.

![New York]({{ site.url }}/images/google-nyc.jpg)

## Interview process

The interview processes at the 3 companies were pretty similar, with a initial HR phone call, followed by multiple technical screens. Of special note is Stripe's, who flew me from Singapore to San Francisco for an on-site interview.

### Google

Initial HR phone call with recruiter, followed by 3 back-to-back technical interviews via phone and Google Docs on the same day. After I passed the technical interviews, there are N phone calls with teams that are interested to pick up an intern. For me, N = 1, but it can vary.

### Stripe

Initial HR phone call with recruiter, technical interview via Skype and shared screen coding, on site with 3 or 4 (can't remember) technical interviews and a lunch with an engineering manager. More details on the on site can be found in this [Quora post](https://www.quora.com/What-is-the-engineering-interview-process-like-at-Stripe).

### Uber

Initial HR phone call with recruiter, followed by 2 technical phone calls with online collaborative IDE, and 1 phone call with a manager.

## Team I was in, projects I worked on

Details will be scarce in this section due to confidentiality, but I try to give a higher level look as to the kind of work interns got at each company.

### Google

Internal tool to convert a service written in old framework style into a service written in the new framework style. This was a internship task that my mentor scoped out for me. I finished this ahead of time, so I went on to another task related to a bot that comments on the internal bug tracker when certain conditions are met.

My project was clearly scoped out to be an intern project: it wasn't anything critical, but was something that an Intern could do and would be helpful to the team. Throughout my internship, I was not involved in the projects that my colleagues were doing.

### Stripe

I was initially given smaller tasks that were on the sprints to get warmed up, so I dealt a little with merchant search (that's the search feature you see if you are a logged into your Stripe dashboard), and also a little with API permission. I had 2 big tasks scoped out by my mentor, the first had to do with the frontend of a new [Connect](https://stripe.com/connect) feature, the second has to do with creating a new data pipeline to calculate fees.

The features that I was tasked with are additions to the core product, especially the data pipeline with actually affects the company's earnings! I felt like the entire team trusts me. My team ran a 2 week sprint system, with weekly sprint meetings, and I was encouraged to participate like a full timer.

### Uber
The first task was to run an experiment on web [sign up form](https://get.uber.com/) to get warmed up. While this was in progress (experiments take a while to run), I was in discussion with my mentor for subsequent tasks. Eventually we settled extracting a microservice, which was the work the rest of my team was going to be working on for the subsequent months.

My team runs a weekly sprint system, and the bigger team that we're part of has a 2-week sprint cycle. I mostly worked within my immediate team, knocking tasks of a task board we set up to track our own tasks.

## Tech stack

### Google

Well known for its giant [monorepo](https://www.wired.com/2015/09/google-2-billion-lines-codeand-one-place/), has extremely well thought out tools for developing, building, testing, etc. Main languages used are C++, Java, Python. A lot of internal tools that are slowly being open sourced, build tool [bazel](http://bazel.io), code search [kythe](https://kythe.io/), etc. Uses internal tool for running servers, open sourced as [kubernetes](http://kubernetes.io/).

### Stripe

Main languages are Ruby and Scala. Uses Github for code, PR, code review, phabricator for issue tracking. Deploys to AWS using a custom tool, and developers can develop on AWS instances too.

### Uber

I worked mainly on Python, phabricator for code review, has a custom tool to deploy, each dev spawns an AWS instance to develop on. There are 2 blog posts that goes into their stack more in depth, encourage you to read them [here](https://eng.uber.com/tech-stack-part-one/), and [here](https://eng.uber.com/tech-stack-part-two/).

## Day to day life

Life was really good at all 3 companies, I felt extremely looked after, to the extent of being pampered.

3 meals were provided at every company. At Google and Uber there would be some special pop-up events, hot chocolate, cupcakes, etc. Google has baristas in house, and they make really good lattes with very pretty art.

There is a weekly 1 on 1 with my mentor where we could talk about anything, problems at work, questions about company, issues settling in etc. Stripe has a interesting culture of taking coffee walks, so all my 1 on 1 at Stripe was done while making our way to a coffee shop.

All 3 companies had a weekly all hands meeting as well, where there would be some presentation and a Q&A with heads of the company.

There are tech talks too, and the frequency correlates with the size of the company.

Office hours are really flexible at all companies, they care more about your output than your hours. Time off can be taken as needed with advance notification.

## That's all folks

I had a really good time at all 3 companies, I felt technically challenged, learned a lot, had very good mentors. If you are interested in applying for an internship and am not sure where to start, check out [Project Intern](https://ymichael.github.io/projectintern/).

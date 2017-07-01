---
author: Jingwen
date: 2015-04-13T10:37:25Z
title: 'Friday Hacks #93, April 17'
url: /2015/04/13/friday-hacks-93-Apr-17/
---

For the final Friday Hacks of the semester, we'll be having Melvin Zhang, lead architect from Cosmiqo International, and Mathieu Feulvarch, senior product architect from MyRepublic. See you!

{% capture venue %}
    {{ 'SR3, Town Plaza, UTown' }}
{% endcapture %}
{% include friday_hack_header.html %}

Facebook Event link: https://www.facebook.com/events/1569158963362746/

### Teleport, an Intelligent Routing Service

#### Talk description

Teleport is MyRepublic's intelligent routing service - a hassle-free,
device-free and cost-free way of allowing subscribers to experience the
Internet it was meant to be enjoyed: smooth and without restrictions. Find out
how it was conceptualised and built, and why it remains as the Industry's most
unique offering in its category.

#### Speaker profile

Mathieu Feulvarch is the Senior Product Architect with MyRepublic and the brain
behind Teleport, the ISP's widely-lauded intelligent routing service. After
discovering his passion for programming at the young age of 7, Mathieu has gone
on to work in France, the US and now, of course, Singapore - bringing his over
20 years of experience to bear in seeking innovative solutions in the
ever-changing Internet landscape.

### Functional Programming from First Principles

#### Talk description

We've heard a number of talks this semester on functional programming
languages such as Elixir and Scala. These languages are large and complicated,
which makes it difficult to understand the essence of functional programming.

Church's Lambda Calculus is the oldest and simplest possible functional
programming language. It has the following syntax:

```<var> ::= a | b | ... | z```

```<exp> ::= <var> | (\<var> <exp>) | (<exp> <exp>)```

In this talk, we will explore Church's Lambda Calculus via a series of demos
based on Tromp's 2012 IOCCC winning entry: http://www.ioccc.org/2012/tromp/hint.html
An unobfuscated version of the above is available at https://github.com/melvinzhang/binary-lambda-calculus and will be used for the demos in this talk.

#### Speaker profile

Melvin is an avid programmer who enjoys designing and implementing novel
algorithms.  As the lead architect of [Cosmiqo](http://cosmiqo.com/), Melvin is in charge of developing its sensor data aggregation and analytics platform. In his spare time, Melvin works on the AI for [Magarena](https://magarena.github.io/), an open source card game project.  Melvin received his B. Comp (Hons) and Ph.D. degrees from NUS School of Computing.

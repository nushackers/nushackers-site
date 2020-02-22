---
author: Jingwen
date: 2015-10-05T00:14:25.000Z
title: 'Friday Hacks #99, Oct 09'
url: /2015/10/friday-hacks-99
---

We're very happy to have two recent graduates of NUS School of Computing to speak at this week's Friday Hacks about a very important programming language construct: the parser. Omer will be introducing what monads are and how you can use them to build parsers, while Richard will give an overview about his FYP that lets you parse and evaluate C code inline in vim.

{{< friday_hack_header venue="Seminar Room 3, Town Plaza, University Town" date="Oct 09" >}}

Facebook Event link: https://www.facebook.com/events/525850107570346/

# Monadic Parsers

In this talk, we'll learn about how to write a programming language parser using a functional programming construct called monads.

It'll be broken down into three steps:

1. Writing some simple functions to parse chars, numbers etc
2. Combining these simple parsers to make more complex parsers using higher order functions (bind)
3. Oh wow, we discovered monads!

Analogies from other languages will also be given to make the concept independent from Haskell.

The talk will be based off this paper: //www.cs.uwyo.edu/~jlc/courses/3015/parser_pearl.pdf

## Speaker profile

Omer is an NUS Hackers alumnus, currently working as an iOS Software Engineer at Garena. He also moonlights as a Haskell proselytizer, and is a little obsessed with writing useless, toy compilers.

# Writing Programming Language Applications: C Worksheet Instrumentor

My FYP has been described as "pretty cool", "more useful than my FYP", and "the best thing to ever happen to C". - A C 'worksheet' program providing live-coding features that are becoming more common thanks to editors such as the LightTable (which gained 300K in its KickStarter).
See https://github.com/rgoulter/c-worksheet.vim

In this presentation, I'll give a sketch as to how to write programs which take in other programs as input, and how these outline how these techniques were applied to write the C worksheet tool.

## Speaker Profile

Richard is a recent graduate of NUS' School of Computing, (not as an exchange student). When he was in his first year as an undergrad he grew such an impressive beard that when he shaved it off none of his friends recognised him even though he was the only angmoh in most of his classes.

---
layout: friday_hack
title: "Friday Hacks #108, March 4th"
date: 2016-02-26 00:00:01
author: Varun
---

For our fourth Friday Hacks of the semester, we're having Cheng Wei, a senior
expert software engineer from Garena Labs to talk about their file store
engine in GoLang.

Facebook Event link:
[https://www.facebook.com/events/1664420683812357/](https://www.facebook.com/events/1664420683812357/)

{% capture venue %}
    {{ 'Seminar Room 3, Town Plaza, University Town' }}
{% endcapture %}
{% include friday_hack_header.html %}


# File Store Engine in Go --- how to reduce GC overhead

### Description
In Garena, we store hundreds of TB of files and serve more than ten thousand file download requests per second. This huge workload requires an efficient file store engine. We chose BeansDB in the beginning, but find it not appropriate when used in the high speed cache system. Finally, we decide to rewrite it in Go language. Although Go is much simpler and more a pleasure to write compared with C, it also introduces a new problem, the GC issue. In this talk, we will go deep in this topic and share the best practices we learnt in reducing GC overhead. Meanwhile, we also show that the Go GC system is still continuous evolving thanks to the effort of Go dev team.

### Speaker's Profile

Cheng Wei obtained his PhD degree from School of Computing, NUS on 2010, and then joined Garena and involved in various of projects there. Since 2013, he worked as server team leader of BeeTalk, a social app having tens of millions of active users. He likes learning new programming languages and is also keen on profiling and optimizing the performance of server programs.

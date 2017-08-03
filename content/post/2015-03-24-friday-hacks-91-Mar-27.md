---
author: Jingwen
date: 2015-03-24T10:37:25Z
title: 'Friday Hacks #91, March 27'
url: /2015/03/24/friday-hacks-91-Mar-27/
---

We'll have two talks this week: Chris (ZALORA) will be talking about how
they built and deployed a large scale web application, while Omer (Garena) will
be talking about Reactive Cocoa, a functional reactive framework for iOS and
OSX.

{{% friday_hack_header venue="SR3, Town Plaza, UTown" date="March 27" %}}

Facebook Event link: https://www.facebook.com/events/1436223633336896/

### Purely Functional Deployments with Nix: Hacking on "Web Scale" Applications
 
#### Talk description

Cloud hosting allows us to build brittle networks out of less reliable components faster than ever before. Tools like Puppet and Docker help manage this complexity, but we can do better. Instead of declaring or packaging the state of an infrastructure, what if we could manipulate it as a data structure?

At ZALORA, we've built the largest known web application infrastructure described by a purely functional program. Using a combination of Nix, NixOS, and our own Upcast, we don't just deploy our networks—we check them into Git. You'll see the steps we took to get here and the concepts we've borrowed from computer science, like metaprogramming, along the way.

#### Speaker profile

Chris joined ZALORA in 2013 after leaving the web startup field in California. He learned to code by hacking together programs on his HP 48G graphing calculator in order to automate his math homework. He started writing web applications in 2001, right after the dot-com crash. You can view some of his code at https://github.com/jekor

### Functional Reactive Programming on iOS
 
#### Talk description

Programs take input, from various sources, transform it, and produce some output. That input could be keyboard events, GPS Signals, time triggers, web responses, or all of them at the same time. Similarly, outputs can be anything from rendering a kitten, to performing an API Request, to flushing a toilet.

Functional Reactive Programming broadly models these input outputs flows as “signals”, which can be composed, and transformed to return new signals. Programs can therefore model their “inputs -> transform -> output” pipelines, explicitly. This has a number of advantages, the most prominent one being the escape from the inevitable callback hell, when modeling and coordinating multiple asynschronous events.

Reactive Cocoa is a powerful FRP framework for Cocoa, which brings these concepts from the “ivory tower” to OSX/iOS land. This talk will take a shallow dive into the framework, showcasing FRP’s usefulness in somewhat real world scenarios.

#### Speaker profile

Omer is an NUS Hackers alumnus, currently working as an iOS Software Engineer at Garena. He also moonlights as a Haskell proselytizer, and is a little obsessed with writing useless, toy compilers.

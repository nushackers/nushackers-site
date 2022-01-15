---
author: Jingwen
date: 2015-01-26T22:08:25.000Z
title: 'Friday Hacks #86, January 30'
url: /2015/01/friday-hacks-86
---

We will be having two talks this Friday! One is on software (databases), the
other one is on hardware (Bluetooth), and both speakers are named Cedric. What
are the chances? See you there!

{{< friday_hack_header venue="NUS Hackerspace, AS6 #02-09" date="January 30" >}}

Facebook Event link: https://www.facebook.com/events/1630037577224179/

### The Absolute Minimum Every Software Developer Needs To Know About Database Indexes by Cedric Chin

#### Talk description

If you’re a software developer, it’s nearly guaranteed that you’ve worked with a database before. But what happens when you find your queries running slowly? How do you debug bad database performance? The truth is, most of us don’t know much about RDMS internals: we just insert and retrieve data and pray that our queries run quickly enough.

The good news? It turns out that the only thing a developer really needs to understand about relational databases is how their indexes work. Most of the performance characteristics of modern RDMSes may be explained through the database index. This talk introduces the data structures these indexes use, how these structures determine query performance, how to read a query plan, and what to think about when designing indexes for your database schema.

#### Speaker profile

Cedric Chin is a product manager at Floating Cube Studios, a mobile development agency located in Singapore and Ho Chi Minh City. He likes Python, Go, green tea and cats. In a previous life, he interned at Viki and Kicksend and ran the NUS Hackers.

### TWI, a Bluetooth Low Energy Wireless Motion Sensor by Cedric Honnet

#### Talk description from the speaker

##### What?

The TWI, Tangible Wireless IMU (Inertial Measurement Unit), is a wireless motion sensor. It is optimized to be ultra low power and tiny, 1 in x 1 in (2.5 cm x 2.5 cm).

TWI is basically composed with an ultra compact 9 axis IMU from Invensense, the MPU-9150 and a BLE cortex M0 from Nordic Semi, the nRF51822.

##### How?
To make the PCB, you can get the gerbers from the OSHpark widget, or you can get the latest version from upverter. It's still a prototype but a detailed bill of material is available here: goo.gl/8yxCDU

I developed the PCB using Upverter so feel free to fork it and improve it! Similarly, feel free to fork the GitHub repo and play with the software...
Enjoy ;)


#### Speaker profile

Cedric Honnet holds a Masters in Embedded Systems from ParisTech, France. He is always enthusiastic about anything at the intersections between Arts and interHacktivity.

He has been a Noisebridge addict since 2012, and has taken over the circuit hacking workshops when Mich wasn't in town. Passionate by music and DJing since the age of 14 (~1995), he started tinkering with electronics and computers when building his own home studio. He gave up school quite early to focus on concrete things such as music or computer hacking, and decided to go back after a few years to advance his understanding of technology. During his engineering studies, he also went to hackerspaces to explore more about physical computing and interactivity.

He worked as firmware engineer and interHacktivist at Sifteo in San Francisco, then co-founded tangib.ly, where he gets to play as in a hackerspace. He got to develop musical instruments, virtual reality bike systems, interactive art, and many other Open Source projects.
He is now working on twiz.io, a Tiny Wireless IMU (motion sensor) that controls music, light, fire, etc. It gives a life to everyday objects, enables people's motion and builds a bridge from the tangible to the digital world.

More here:
hacks.honnet.eu
noisebridge.net/user:cedric

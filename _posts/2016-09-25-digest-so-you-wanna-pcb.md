---
layout: post
title: "Digest: Do you wanna PCB?"
date: 2016-09-25 12:00
author: 50m3 b01k3
categories: [Digest]
---

The [scHnRk](https://github.com/nushackers/scHnRk) and [Neander](https://github.com/jellyjellyrobot/neander) was born in the first half of this year.

Designed and Assembled in Singapore, these boards represent leaps of faith into the unknown world of electronics fabrication.

If you're starting out electronics design, this article is for you!

### Prerequisites

You should find yourself a working electronics lab with a functioning set of tools
- multimeter
- power supply
- soldering iron
- oscilloscope

You can access these tools at [Ida Labs @ NLB/NDC](https://www.ida.gov.sg/Programmes-Partnership/Store/IDA-Labs), [HackerspaceSG](https://hackerspace.sg), [Ground Up Intiative](http://groundupinitiative.org/), [One Maker Group](http://onemakergroup.sg) and [NUS Hackerspace](http://www.comp.nus.edu.sg/maps/venues/).

Try to find some money as electronics don't really come cheap :D

### Design

The best designs often start with a meaningful problem, and the passion to follow it through to its solution.

#### Breadboarding

Unless you're designing [something peculiar](http://electronics.stackexchange.com/questions/2103/when-to-avoid-using-a-breadboard), remember to breadboard your designs while laying the schematics out on the CAD software! This way you 
- have an idea of what connections need to be made
- can iron out potential issues with individual components (incompatiblity, interferences, power requirements)

#### Software

In terms of which CAD software to use, I'd recommend KiCad because it's
- open source
- "limitless"

#### Visualization

Most PCB vendors ship your designs immediately to the board house. This means that you cannot edit your boards after submission. One of the most common issues with PCB design is alignment errors.

You may want to check your PCBs for these issues with an online tool such as [webGerber](http://mayhewlabs.com/webGerber/).

#### Sourcing Materials

The best way to get your hands on some scrummy electronics is [Element14](http://sg.element14.com) and [Taobao](https://taobao.com). If you're unsure about Chinese, get some Chinese guy to help you!

#### Microcontroller programming

Some microcontrollers have propietary interfaces that allows you to program the microcontrollers "in circuit". These interfaces are usually called [iscp]s or [jtag] you may want to check out how they work.

When you program them in the assembled PCBs, you may consider investing in a set of [test pins](https://img.alicdn.com/imgextra/i3/179947408/TB2x2wgsFXXXXX_XXXXXXXXXXXX_!!179947408.jpg)/[clips](https://cdn.instructables.com/F28/HXRJ/IBYX1OC4/F28HXRJIBYX1OC4.MEDIUM.jpg).

### Prototyping

This process really depends on the scope of your product and reach.

#### How many prototyping phases?

Excluding breadboarding, you should have at least 2 prototyping phases. This way you can rectify any [wrinkles](http://twitter.com/zxcvgm/status/741057757533458433/photo/1?ref_src=twsrc%5Etfw) in your design.

#### PCB vendors

Most PCB vendors usually take on the order of a week to a month to fulfill your order. I'd recommend getting the rush option.

You can test a variety of PCB vendors to see which one gives you the best bang for bucks. I'd recommend [OSHPark](https://oshpark.com/), [dirtyPCBs](http://dirtypcbs.com/) and [seeedstudio](https://www.seeedstudio.com/fusion_pcb.html).

#### Making your first board

Electronics don't assemble themselves. Allocate about 1-2 minutes per component for assembly. Seasoned soldering people can take as little as 10 seconds to populate one component.

#### To PCB with Chemistry

Understand the [chemistry](https://learn.adafruit.com/adafruit-guide-excellent-soldering/common-problems) behind soldering. It will guide you to
- better maintainence of the soldering iron
- easier soldering experience

### Production/Assembly

You can get away with soldering low component count boards (up to 5 boards). For added ease, you may consider [PCB.NG](http://pcb.ng/index.html).

For assemblies of more than 5 boards, I'd recommend getting PCB Assembly services like [seeedstudio's](https://www.seeedstudio.com/fusion_pcb.html) for peace of mind! Test your designs first as they may be hard to interpret at the assembler's side -> you may get parts in the wrong orientation or placement!

### Other resources

There are many writeups of people in similar positions and I think you can benefit from [one](http://irq5.io) or [two](https://makerforce.io/author/sudharshan/) or maybe [three](https://www.bunniestudios.com).


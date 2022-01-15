---
author: Luther Goh Lu Feng
categories:
  - Guest blogger
comments: true
date: 2008-10-11T00:00:00.000Z
title: Wubi-ing Ubuntu 8.10 Intrepid Beta
url: /2008/10/wubi-ing-ubuntu-810-intrepid-beta/
aliases:
  - /2008/10/11/wubi-ing-ubuntu-810-intrepid-beta/
---

One benefit I enjoy working at <a href="//www.tylerprojects.com/">Tyler Projects</a> was the freedom in choosing the operating system I want. My PC is quite a powerful machine, with 2 GB ram and dual cores. It ran Vista quite seamlessly. I decided to install <a href="//www.ubuntu.com/">Ubuntu Linux</a> I could have easily setup a dual boot but I decided to take this opportunity to try out the <a href="//wubi-installer.org/">Wubi</a> installer for the first time. For those not in the know, Wubi allows you to install and uninstall Ubuntu as any other Windows application, in a simple way that is hardly rocket science.

<div align="center">
{{< imglink src="/img/2008/10/wubi_logo.gif" alt="" >}}</div>

A quick check on the wubi website, showed that the only the installer for Ubuntu 8.04.1 is available for download, despite that the latest 8.10 (codenamed Intrepid) beta has already been released on 2nd Oct. I was sorely disappointed, and was sore enough to rant at <a href="//ubuntuforums.org/">Ubuntu Forums</a>. Thankfully, I found out <a href="//ubuntuforums.org/showthread.php?t=920502">here</a> that it is possible to install Intrepid beta using a snapshot of <a href="//www.wubi-installer.org/devel/minefield/">Wubi minefield</a>. And off I went to download <a href="//www.wubi-installer.org/devel/minefield/Wubi-8.10-rev510.exe">Wubi-8.10-rev510.exe</a>.

The installation is pretty idiot proof. Just double click on the downloaded executable and fill in the details before clicking install:

{{< imglink src="/img/2008/10/wubi-123_small.png" alt="" >}}

Next choose when to reboot:

{{< imglink src="/img/2008/10/wubi-reboot.png" alt="" >}}

Upon rebooting, there will be a black selection menu showing the choice of windows and Ubuntu to boot into. And there I had it, an Ubuntu system :)

<div align="center">{{< imglink src="/img/2008/10/boot-screen.jpg" alt="" >}}</div>

Removal of an Wubi installation is pretty simple. Just go to Control Panel and remove Ubuntu. Done! No more messing of MBRs unless you still want to setup a dual boot :)

{{< imglink src="/img/2008/10/wubi-uninstall_small.png" alt="" >}}

Sounds simple enough and raving to try? Check out the <a href="//wubi-installer.org/faq.php">FAQ</a> before you proceed. And feel free to drop by #linuxnus if you need any help. Or just drop by for some chatter :) Once again, the guide is on our <a href="//opensource.nus.edu.sg/wiki/index.php/Connecting_to_IRC">wiki</a>.

PS. While this post may be a bit newbie, I will be writing another post over the weekend that is more advanced over the weekend. So stay tuned.

<em>All images are from <a href="//wubi-installer.org">//wubi-installer.org</a></em>.

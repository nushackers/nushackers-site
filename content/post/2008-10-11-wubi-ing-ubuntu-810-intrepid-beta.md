---
author: Luther Goh Lu Feng
categories:
- Guest blogger
comments: true
date: 2008-10-11T00:00:00Z
title: Wubi-ing Ubuntu 8.10 Intrepid Beta
url: /2008/10/11/wubi-ing-ubuntu-810-intrepid-beta/
---

One benefit I enjoy working at <a href="http://www.tylerprojects.com/">Tyler Projects</a> was the freedom in choosing the operating system I want. My PC is quite a powerful machine, with 2 GB ram and dual cores. It ran Vista quite seamlessly. I decided to install <a href="http://www.ubuntu.com/">Ubuntu Linux</a> I could have easily setup a dual boot but I decided to take this opportunity to try out the <a href="http://wubi-installer.org/">Wubi</a> installer for the first time. For those not in the know, Wubi allows you to install and uninstall Ubuntu as any other Windows application, in a simple way that is hardly rocket science.

<div align="center">
<a href='/res/2008/10/wubi_logo.gif'><img src="/res/2008/10/wubi_logo.gif" alt="" title="wubi_logo" width="256" height="80" class="aligncenter size-full wp-image-98" /></a></div>

A quick check on the wubi website, showed that the only the installer for Ubuntu 8.04.1 is available for download, despite that the latest 8.10 (codenamed Intrepid) beta has already been released on 2nd Oct. I was sorely disappointed, and was sore enough to rant at <a href="http://ubuntuforums.org/">Ubuntu Forums</a>. Thankfully, I found out <a href="http://ubuntuforums.org/showthread.php?t=920502">here</a> that it is possible to install Intrepid beta using a snapshot of <a href="http://www.wubi-installer.org/devel/minefield/">Wubi minefield</a>. And off I went to download <a href="http://www.wubi-installer.org/devel/minefield/Wubi-8.10-rev510.exe">Wubi-8.10-rev510.exe</a>.

The installation is pretty idiot proof. Just double click on the downloaded executable and fill in the details before clicking install:

<a href='/res/2008/10/wubi-123_small.png'><img src="/res/2008/10/wubi-123_small.png" alt="" title="wubi-123_small" width="500" height="313" class="aligncenter size-full wp-image-103" /></a>

Next choose when to reboot:

<a href='/res/2008/10/wubi-reboot.png'><img src="/res/2008/10/wubi-reboot.png" alt="" title="wubi-reboot" width="500" height="386" class="aligncenter size-full wp-image-100" /></a>

Upon rebooting, there will be a black selection menu showing the choice of windows and Ubuntu to boot into. And there I had it, an Ubuntu system :)

<div align="center"><a href='/res/2008/10/boot-screen.jpg'><img src="/res/2008/10/boot-screen.jpg" alt="" title="boot-screen" width="440" height="287" class="aligncenter size-full wp-image-101" /></a></div>

Removal of an Wubi installation is pretty simple. Just go to Control Panel and remove Ubuntu. Done! No more messing of MBRs unless you still want to setup a dual boot :)

<a href='/res/2008/10/wubi-uninstall_small.png'><img src="/res/2008/10/wubi-uninstall_small.png" alt="" title="wubi-uninstall_small" width="500" height="375" class="aligncenter size-full wp-image-102" /></a>

Sounds simple enough and raving to try? Check out the <a href="http://wubi-installer.org/faq.php">FAQ</a> before you proceed. And feel free to drop by #linuxnus if you need any help. Or just drop by for some chatter :) Once again, the guide is on our <a href="http://opensource.nus.edu.sg/wiki/index.php/Connecting_to_IRC">wiki</a>.

PS. While this post may be a bit newbie, I will be writing another post over the weekend that is more advanced over the weekend. So stay tuned.

<em>All images are from <a href="http://wubi-installer.org">http://wubi-installer.org</a></em>.

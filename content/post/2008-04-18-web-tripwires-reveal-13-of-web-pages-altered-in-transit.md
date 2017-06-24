---
author: Ruiwen
categories:
- Uncategorized
comments: true
date: 2008-04-18T00:00:00Z
title: '"Web tripwires" reveal 1.3% of web pages altered in transit'
url: /2008/04/18/web-tripwires-reveal-13-of-web-pages-altered-in-transit/
---

<blockquote>When you visit a web page, you might expect that the code and images from the page will make their journey through the tubes unmolested and unaltered, but according to security researchers, you would also be wrong 1.3 percent of the time.</blockquote>
Quoting from a <a href="http://arstechnica.com/news.ars/post/20080416-research-1-3-percent-of-web-pages-altered-in-transit.html">recent article</a> on <a href="http://arstechnica.com">Ars.Technica</a>, researchers have found that up to 1.3% of web pages are altered in transit between the server and the requesting client. Not all the modifications are malicious though, the article notes. Some ISPs modify the page either by removing extra white space in the page, or further compressing images, thereby reducing bandwidth used and decreasing wait times. Alternatively, some service providers <a href="http://blog.dk.sg/2008/01/07/creative-advertisement-on-google-main-page/">take the opportunity</a> <a href="http://www.sgwebhostingtalk.com/showthread.php?t=12576">to serve ads</a> instead.

In 2007 (I think), some folks from the <a href="http://www.washington.edu/">University of Washington</a> and the <a href="http://www.icsi.berkeley.edu/">International Computer Science Institute</a> put up a page  to test if pages loaded from various domains were edited while passing through through the 'tubes. Enter the <a href="http://vancouver.cs.washington.edu/">UW CSE and ICSI Web Integrity Checker</a>.

Here's quoting their results so far:
<ul>
	<li>50,171 unique IP addresses visited the page.</li>
	<li>657 IP addresses reported modified pages (1.3%).</li>
	<li>70% of the modifications where caused by client-side proxy software, such   as ad blockers and popup blockers.</li>
	<li>46 IP addresses reported changes that were caused by an ISP, such as   injected advertisements and modifications to reduce network traffic.</li>
	<li>125 IP addresses were using proxies that caused them to be vulnerable   to cross site scripting attacks.</li>
	<li>3 IP addresses were affected by adware or worms.</li>
</ul>
I'm curious as to how this test would fare in Singapore. Are our local providers editing the pages we request on the fly? So here's what, just for fun,
<ol>
	<li>Perform the test by visiting <a href="http://vancouver.cs.washington.edu/">the page</a></li>
	<li>Then, visit <a href="http://opensource.nus.edu.sg/wiki/index.php/Web_Integrity">this page</a> on the linuxNUS <a href="http://opensource.nus.edu.sg">Opensource Wiki</a> to record your results</li>
</ol>
Let us know how it went!

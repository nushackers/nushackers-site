---
layout: friday_hack
title: "Friday Hacks #131, March 17"
date: 2017-03-13 09:52:54.484766
author: Jethro Kuan
---

Hi folks! This week we are privileged to have one of the leading experts in high performance computing (he has his own law!), give a talk on the intricacies of math in computing. For more information, refer to the talk description.

{% capture venue %}
    {{ SR3, Town Plaza, University Town, NUS }}
{% endcapture %}
{% include friday_hack_header.html %}


### Weapons of Math Destruction

#### Talk Description:
A new data type called a "posit" is designed for direct drop-in replacement for IEEE Standard 754 floats. Unlike unum arithmetic, posits do not require interval-type mathematics or variable size operands, and they round if an answer is inexact, much the way floats do. However, they provide compelling advantages over floats, including simpler hardware implementation that scales from as few as two-bit operands to thousands of bits. For any bit width, they have a larger dynamic range, higher accuracy, better closure under arithmetic operations, and simpler exception-handling. For example, posits never overflow to infinity or underflow to zero, and there is no "Not-a-Number" (NaN) value. Posits should take up less space to implement in silicon than an IEEE float of the same size. With fewer gate delays per operation as well as lower silicon footprint, the posit operations per second (POPS) supported by a chip can be significantly higher than the FLOPs using similar hardware resources. GPU accelerators, in particular, could do more arithmetic per watt and per dollar yet deliver superior answer quality.

A series of comprehensive benchmarks compares how many decimals of accuracy can be produced for a set number of bits-per-value, using various number formats. Low-precision posits provide a better solution than "approximate computing" methods that try to tolerate decreases in answer quality. High-precision posits provide better answers (more correct decimals) than floats of the same size, suggesting that in some cases, a 32-bit posit may do a better job than a 64-bit float. In other words, posits beat floats at their own game. 

#### Speaker Profile
NUS Professor Dr. John L. Gustafson is an applied physicist and mathematician. He is a former Director at Intel Labs and former Chief Product Architect at AMD. A pioneer in high-performance computing, he introduced cluster computing in 1985 and first demonstrated scalable massively parallel performance on real applications in 1988. This became known as Gustafson's Law, for which he won the inaugural ACM Gordon Bell Prize. He is also a recipient of the IEEE Computer Society's Golden Core Award.

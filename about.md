---
title: About
layout: post
permalink: /about/
notes: |
  <h3>What is Hacking?</h3>

  <p>The simplest way to define hacking is: 'playful cleverness'. We usually take it to mean the act of creating interesting software, but 'playful cleverness' may be applied to all sorts of things: life, music, hardware, food. <a href="/hackerdefined/">More on this →</a></p>

  <h3>Formerly linuxNUS</h3>

  <p>We were formerly known as linuxNUS, an open source advocate in NUS. We have since changed our name to reflect the shifting nature of our organization: we now spend more time promoting hacking, programming-for-fun, and free/open-source-software use in the NUS community. <a href="/name-change/">More on the name change →</a></p>

---

In the jargon of the computer programmer, a hacker is someone who strives to solve problems in elegant and ingenious ways. NUS Hackers is a student-run organization committed to the spread of hacker culture &amp; free/open-source software. We provide a support system for hackers in NUS who are currently building things (be it for charity, business or pleasure). We also hold workshops, run   technical meetups, organize hackathons, and maintain open source code for the NUS community.

###<a name="what-we-do"></a>What We Do

We have weekly meetups every Friday called [Friday Hacks](/fridayhacks/). They include one or two technical talks, followed by a hacking session.

Every semester, we run a series of technical workshops called [hackerschool](http://school.nushackers.org/). We also run the Hack&amp;Roll hackathon in the second semester of the academic year. Our coreteam members contribute to events like LadyPy and Software Freedom Day.

We maintain and release open source code for the NUS community (see: our [code page](/code/)). Students and staff who have built NUS-specific projects and can no longer maintain them may come to us to host and maintain their code.

We currently maintain [Download@NUS](http://download.nus.edu.sg/) We have a team working with the NUS Computer Centre to host linux mirrors.

###<a name="philosophy"></a>Philosophy

We believe that hacking is necessary for good innovation. (In fact, the best computer-related startups and technologies [have all come from hackers](/why/)). As an extension to that, we think tinkering is win-win-win: you learn new things, you get to show off, and you become more attractive to employers.

(Though, honestly, most of the time we hack because we think it's fun).

###<a name="goal"></a>Goal
Our long term goal is to build a healthy community of passionate hackers in NUS. We think that this benefits everyone: professors benefit because they are able to source for good programmers; startups and tech companies benefit because they are able to recruit from a central pool; students benefit because they get to meet and learn from like-minded peers (and get opportunities, i.e.: from professors and tech companies).

###<a name="management"></a>Management

NUS Hackers is managed by a coreteam of student-volunteers. If you'd like to request a workshop, get us to publicize your code, or ask us a question, we recommend that you [send us an email](/contact/).

###<a name="current-coreteam"></a>Current Coreteam

{% for person in site.data.coreteam_members %}
<p>
    <strong>
        {{ person.name }}
        {% if forloop.first %}
            [President]
        {% endif %}
    </strong> is {{ person.description }}
</p>
{% endfor %}


###<a name="alumni"></a>Alumni
We keep a list of former NUS Hackers coreteam members [over at our alumni page →](/alumni/)

###<a name="join-us"></a>Join us
Want to help us spread the hacker culture? You can find out more [here](/join_coreteam/).

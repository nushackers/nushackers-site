---
title: About
layout: post
permalink: /about/
notes: |
  <h3>What is Hacking?</h3>

  <p>The simplest way to define hacking is: 'playful cleverness'. We usually take it to mean the act of creating interesting software, but 'playful cleverness' may be applied to all sorts of things: life, music, hardware, food. <a href='/hackerdefined/'>More on this →</a></p>

  <h3>Formerly linuxNUS</h3>

  <p>We were formerly known as linuxNUS, an open source advocate in NUS. We have since changed our name to reflect the shifting nature of our organization: we now spend more time promoting hacking, programming-for-fun, and free/open-source-software use in the NUS community. <a href='/name-change/'>More on the name change →</a></p>

---

In the jargon of the computer programmer, a hacker is someone who strives to solve problems in elegant and ingenious ways. NUS Hackers is a student-run organization committed to the spread of hacker culture &amp; free/open-source software. We provide a support system for hackers in NUS who are currently building things (be it for charity, business or pleasure). We also hold workshops, run hackfests, and maintain open source code for the NUS community.
<h3>What We Do</h3>
We have weekly meetings every Friday called <a href="/fridayhacks/">Friday Hacks</a>. They include one or two technical talks, followed by a hacking session.

Once a year, we run a series of technical workshops called <a href="http://school.nushackers.org/">hackerschool</a>. We also run the Hack&amp;Roll hackathon in the second semester of the academic year. Our coreteam members contribute to events like LadyPy and Software Freedom Day.

We maintain and release open source code for the NUS community (see: our <a href="/code/">code page</a>). Students and staff who have built NUS-specific projects and can no longer maintain them may come to us to host and maintain their code.

We currently maintain <a href="http://download.nus.edu.sg/">Download@NUS</a>. We have a small team of people working with the NUS Computer Centre to host scientific data. We also have a small team of hardware hackers who meet at Friday Hacks.
<h3>Philosophy</h3>
We believe that hacking is necessary for good innovation. (In fact, the best computer-related startups and technologies <a href="/why">have all come from hackers</a>). As an extension to that, we think tinkering is win-win-win: you learn new things, you get to show off, and you become more attractive to employers.

(Though, honestly, most of the time we hack because we think it's fun).
<h3>Goal</h3>
Our long term goal is to build a healthy community of passionate hackers in NUS. We think that this benefits everyone: professors benefit because they are able to source for good programmers; startups and tech companies benefit because they are able to recruit from a central pool; students benefit because they get to meet and learn from like-minded peers (and get opportunities, i.e.: from professors and tech companies). We think we are 2, 3 years away from this goal.
<h3>Management</h3>
NUS Hackers is managed by a coreteam of student-volunteers. If you'd like to request a workshop, get us to publicize your code, or ask us a question, we recommend that you <a href="/contact/">send us an email</a>.
<h3>Current Coreteam</h3>

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


<h3>Alumni</h3>
We keep a list of former NUS Hackers coreteam members <a href="/alumni/">over at our alumni page →</a>

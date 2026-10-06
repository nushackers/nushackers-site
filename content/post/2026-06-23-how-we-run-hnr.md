---
title: "How We Run Hack&Roll"
date: 2026-10-05
author: Jonathan Loh
url: /2026/10/how-we-run-hnr
featured: true
---

How does our relatively small coreteam pull off an 800+ person hackathon? Mostly by splitting this huge event into many small pieces, then trusting coreteam to take ownership of them. Hacker culture is built into the way we do things. Over the years, people have asked us how we run Hack&Roll, so here is a look inside coreteam, from my small perspective.

> The opinions in this post are my own and do not necessarily reflect those of NUS Hackers coreteam. Grammar and phrasing was fixed with AI so you guys don't have to read my verbose vomit...

Of course, this is a simplified view of the work. In the week of Hack&Roll, the Discord is full of people asking for updates, checking whether something has arrived, and trying to make one more thing work before participants arrive. This is part of the fun of coreteam: everyone has their own workgroup, but nobody gets to stay in it all weekend.

## What is Hack&Roll?

If you've never been to Hack&Roll,

- It is a 24-hour, in-person hackathon where students build anything they want
- Throughout the event, we provide free food, fun games, and good vibes over one weekend
- In recent years, it has been held in NUS University Town with Hack&Roll 2026 welcoming more than 800 participants

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; padding: 20px 0 5px;">
  <img src="/img/2026/hnr/1.webp" alt="Participants working on their projects in CAPTxRC4 Dining Hall" style="width: 30rem" />
  <img src="/img/2026/hnr/2.webp" alt="Participants working on their projects in RC4 MPSH" style="width: 30rem" />
</div>

NUS Hackers' coreteam runs this event, alongside others like [Friday Hacks](/fridayhacks/) and [Hackerschool](/hackerschool/), to [**spread hacker culture**](/hackerdefined/). Coreteam aims to encourage people to build for the fun of it, not because of some problem statement - we don't need everyone to save the world. This hacker culture mindset shapes our decisions: whenever we choose what to build, buy, or prioritize, we ask whether it helps people try building something.

## Small Team, Big Ownership

In 2026, coreteam had approximately 30 members, not all of whom were based locally in Singapore. We organize ourselves into small workgroups. Each group owns a part of the event, but no one works in isolation.

As a high level overview, we are organized into the workgroups with these principles:

- **Keep workgroups small** (usually 2–4 people): This keeps the work manageable and makes it clear who owns each part of the job
- **Each coreteam is responsible for 2–3 workgroups**: This encourages cross-team collaboration and gives organizers a chance to understand more of the event than just their own area

This only works if we tetris our people and time with some thought. e.g. someone handling AV should not also be responsible for sponsorship setup if both need to happen at the same time before the opening ceremony. While we want to optimize such that every coreteam gets to do what they want, sometimes what they want may conflict in real operational timelines.

Of course, in the week before Hack&Roll, this is more chaotic - our volunteers will tell you the number of last minute changes, but that's part and parcel of what we do.

<div style="display: flex; justify-content: center; padding: 20px 0 5px;">
  <img src="/img/2026/hnr/organisers-2026.webp" alt="Hack&Roll 2026 organisers gathered for a group photo" style="width: 32rem; max-width: 100%; height: auto" />
</div>

## What this looks like on the ground

Click on each of the workgroups below to see how they function! These are not exhaustive, since there are many small jobs which do not fit cleanly into one team, but they give you a sense of what coreteam spends our time doing.

<div class="workgroups">
  <details>
    <summary>AV</summary>
    <p>This year, we invested more effort into AV (audio visual) setup: the sound setup, video projections, and streaming across different venues. The stage backdrop was also initiated by the AV team, and executed by the design team to make the event "fuller". Returning participants may have noticed that the setup was a major step up from previous years. That was possible because we had both people who already knew the systems and people willing to learn. We even set up our own RTSP server to avoid music copyright strikes when streaming on external services like YouTube. It was a ridiculous number of hurdles, but the AV team kept jumping over them. As someone who learnt AV from projections, to sound mixing, it's honestly not ridiculously hard, it just takes some time and effort to sit down and play around with the systems.</p>
  </details>

  <details>
    <summary>Food</summary>
    <p>Often the most memorable part of our event is food. However, a lesser known fact is how we ensure sufficient quantity and quality. In true hacker mindset, we enjoy making data-driven decisions. We ask participants to scan their tags / hardware badges for their first portion of food, allowing us to make better informed decisions on how many portions to cater for participants. There's also more to it than just "order food for 800 people", buffet line positioning, timings, etc all have to be factored in. As if that wasn't enough work, the various food carts like coffee and ice cream carts also require independent coordination! Kudos to our food team!</p>
    <div style="display: flex; justify-content: center; padding: 20px; padding-top: 5px;">
      <img src="/img/2026/hnr/food-line-2026.webp" alt="Hack&Roll participants and volunteers at the food line in the main hall" style="width: 24rem; max-width: 100%; height: auto" />
    </div>
  </details>

  <details>
    <summary>Fringe Events</summary>
    <p>Fringe Events runs the games that let participants take a break from their hacks. Over the years, this has included Tetris, Typeracer, Duck Hunt, Esolang, and board games. Small games and events like this keep the event more lively, especially going into the dreaded 8-12h mark at night when nothing is working. The team has to handle the game rules, game masters, venues, timings and prizes, which is more work than it sounds like when the plan is simply "let's play Tetris". A common problem is realizing 5 minutes before the event that the free tier cannot accommodate our 800 participants and scrambling for someone with a subscription, or an alternate platform (yes, better hindsight could've been used, but things like that do happen when we've got other stuff to prepare for too!).</p>
    <div style="display: flex; justify-content: center; padding: 20px; padding-top: 5px;">
      <img src="/img/2026/hnr/typeracer-2026.webp" alt="A participant plays Typeracer during Hack&Roll 2026" style="width: 30rem; max-width: 100%; height: auto" />
    </div>
  </details>

  <details>
    <summary>Hardware</summary>
    <p>Hardware used to be mostly about loaning equipment to participants. In 2026, we expanded this into our first custom PCB badge, so participants could not only borrow hardware but also hack on the thing they were wearing. With more than 1000 badges prepared for an event with over 800 participants, this was probably the biggest badgelife event in Singapore at the time. (thanks to the team, including some volunteers who we onboarded earlier, who pulled this off!) The badge had to be designed, soldered, flashed, distributed, explained, and then supported when people tried to make it do more. It was a lot of work, but seeing participants colour and hack on their badges was such a huge W! We took an L because the badge was rather heavy with the batteries and we had to hand solder the battery holder and reprogram the NFC on each badge too. But nonetheless, the feedback turned out great!</p>
    <div style="display: flex; justify-content: center; padding: 20px; padding-top: 5px;">
      <img src="/img/2026/hnr/badges.webp" alt="Colored custom PCB badges" style="width: 18rem" />
    </div>
  </details>

  <details>
    <summary>Volunteers</summary>
    <p>Coreteam plans Hack&Roll but the 30+ of us would be unable to run it without our volunteers. Before the event, the coreteam prepare the volunteer schedule and briefing. During the event, our volunteers help with registration, food, swag, booths, crowd movement, and all the small tasks that appear when 800 people are in the same place. Many participants also come back as volunteers and experience Hack&Roll as an organizer too.</p>
  </details>

  <details>
    <summary>Judging</summary>
    <p>This year, we expanded judging to work across multiple venues (3 venues spaced ~30m apart), hundreds of projects and more than a hundred judges. The team recruits and briefs judges, prepares the modified <a href="https://github.com/anishathalye/gavel">Gavel</a> and judging system, prints venue maps, and helps judges find the teams' locations. It is also one of the places where the Webapp and Venue teams have to work closely, because a judging process that looks simple on paper can become confusing when people are walking between halls. The team also optimizes for judging experience, ensuring each team gets judged fairly. We've been gradually expanding this team as it involves such a wide scope from technical development to judges outreach and administrative work.</p>
    <div style="display: flex; justify-content: center; padding: 20px; padding-top: 5px;">
      <img src="/img/2026/hnr/judges-2026.webp" alt="Hack&Roll 2026 judges gathered in an auditorium" style="width: 30rem; max-width: 100%; height: auto" />
    </div>
  </details>

  <details>
    <summary>Prizes</summary>
    <p>Prizes starts long before the prize ceremony. The team decides what categories we want to reward, keeps track of the prizes, and works with Judging and Sponsorship so that the awards are ready when the projects are. It sounds straightforward until your order is cancelled one week before the event - with 15+ different orders, this is bound to happen unfortunately.</p>
  </details>

  <details>
    <summary>Publicity</summary>
    <p>Publicity is how people hear about Hack&Roll before they know they want to attend. They write announcements, prepare posts, publicise the workshops, and get the word out about Hack&Roll. Sending the word out to various different schools and societies is particularly challenging. As it stands, keeping this post short and brief was... a tall order.</p>
  </details>

  <details>
    <summary>Design</summary>
    <p>Design is responsible for making Hack&Roll look like Hack&Roll. This includes the posters around the event, but also the registration booth, coffee cart, stickers, shirts, badges, backdrops and other small details that appear everywhere during the weekend. It is easy to only notice design when something looks bad, so the team does a lot of work that participants hopefully never have to think about. I'm sure many of you loved the posters from last year too as we had many people asking us if they could bring them home!</p>
  </details>

  <details>
    <summary>Registration</summary>
    <p>Registration is the first workgroup most participants meet. They handle the registration form, selection, acceptance emails, team appeals and day-of check ins. During Hack&Roll, this also connects to the Webapp, QR codes, participant tags, lanyards, and the physical process of getting hundreds of people into the venue without making everyone queue forever. This last part is particularly hard because throwing more people at the problem frequently causes a larger mess and confusion. With such high load and movement, there are bound to be problems. Backup processes are also in place when Supabase (historically Firebase) authentication goes down, or for example in 2025, we accidentally tagged badges to the wrong participants.</p>
  </details>

  <details>
    <summary>Sponsorship</summary>
    <p>The food and atmosphere of Hack&Roll only exists because our sponsors help us make them happen. The Sponsorship team finds and works with these sponsors/partners, then coordinates with the rest of coreteam to turn that support into workshops, hardware, food, prizes, and other parts of the event. There is also a lot of followup emails and last minute coordination, which is less visible than simply confirming a sponsor via email, but takes up a lot of time. As an organization working with so many sponsors, we aim to keep the sponsor experience and tiers fair - balancing a fun & enjoyable event, sponsor benefits, and sponsor visibility. The sponsorship team frequently requires additional contextual knowledge of the entire event to present to sponsors as well, they serve as the frontdesk of Hack&Roll for companies, providing information about the event where possible.</p>
  </details>

  <details>
    <summary>Swag</summary>
    <p>Swag is a surprisingly large physical logistics problem. Someone has to decide what participants receive, coordinate the items arriving, sort them, move them to the right venue, and hand them out. Some of it arrives much later than we would like, which makes the midnight surprise especially exciting for the people who have to pack it. Hack&Roll has enough swag that this can turn into a whole operation by itself, especially when we try to give things out fairly without making the collection process take the entire night. Recurring participants would know by now how the long snake forms around the main venue around 23:55 at night, so I guess the midnight surprise isn't so surprising anymore.</p>
    <div style="display: flex; justify-content: center; padding: 20px; padding-top: 5px;">
      <img src="/img/2026/hnr/swag-2026.webp" alt="Organisers sorting and distributing Hack&Roll 2026 swag" style="width: 30rem; max-width: 100%; height: auto" />
    </div>
  </details>

  <details>
    <summary>Venue</summary>
    <p>The Venue workgroup is in charge of booking all our venues: the main dining hall, side venue halls, ops rooms and logistics storerooms. They are one of the earliest teams to start, because we cannot host 800 in-person participants if we are missing even one of these spaces. There is a surprising amount of planning in deciding not just where people hack, but where food, workshops, judging, hardware and coreteam can all fit. We also need to book rooms for the workshops before the main event, which means this work starts long before most participants have heard of Hack&Roll. They also take care of the "physical infra" of the event - this includes tables, chairs, trash bags, power, signage, room setup, and fighting fires throughout the event. During the event, they are usually moving between halls and solving problems before most participants notice them. If a trash bag is suddenly overflowing, this is usually the team that gets called.</p>
  </details>

  <details>
    <summary>Workshops</summary>
    <p>Workshops happen before the main 24 hours, and are a way for participants to try something before they start building. The team coordinates instructors, materials, rooms and schedules, including technical workshops where participants get to use hardware they may not have tried before. They also need to update the Hack&Roll page, publish the forms, and remind people who signed up to actually show up. Every workshop is its own small event, so a lot of work goes into making the 2 hour workshop on the schedule look easy. They also get ridiculously sick of eating pizza for dinner 1-2 weeks consecutively.</p>
  </details>

  <details>
    <summary>Webapp</summary>
    <p>The Webapp workgroup builds many of the parts of Hack&Roll that people use without thinking about them: registration, the participant dashboard, check in, food and swag collection, judging, and fringe games. It also has to connect to the physical event, where a QR code, tag or scanner is often involved. The team is also regularly asked to remove friction from everyone else's work, whether that means better navigation during registration, syncing the judging system, or making it easier for participants to find information without searching through Discord. The goal is for the normal flow to be boringly simple. Ensuring the relevant teams test their workflow proves to be hard when we are scrambling in our own other teams a week before the event.</p>
  </details>
</div>

## What keeps it together

Running Hack&Roll is not about one person having the whole plan. The work is distributed, but the responsibility and ownership is shared: groups have the agency to make decisions, people help outside their usual areas, and team members learn what they do not already know. That is how coreteam makes such a large event feel welcoming, chaotic, and fun at the same time.

After attending Hack&Roll as a participant for 3 years and serving on coreteam for 2, I'm still grateful to everyone who makes it happen: past and present coreteam members, participants, volunteers, judges, and sponsors. The best part is not simply that we run Singapore's largest student-run hackathon. It is that the event gives people a reason to build for fun.

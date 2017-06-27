# nushackers-site

Sup! This is the source code of the nushackers blog site http://nushackers.org.
Development blog site at https://nushackers.netlify.com

## Requirement

This website is built with hugo, so if you want to make changes to the templates or structures of the site, please first read about [hugo](https://gohugo.io/overview/introduction/). But if you are just going to modify the data or update/add a post, you can simply follow the guide below.

## Getting started

It's recommended that you test the site locally before doing any push. To do so, first install [hugo v0.24]("https://github.com/gohugoio/hugo/releases") and [node lts](https://nodejs.org/en/).

Then enter this folder and run

```bash
npm install
npm start
```

Hugo will now generate the site and watch the directory and update the site when any changes are made. You can access the site at `http://localhost:4000`

## Updating data

First, since hugo uses [yaml]("http://en.wikipedia.org/wiki/YAML") as the markup for data. It's really simple, so just read about it first.

With some knowledge of yaml, you can take a look at the `content` folder - it contains the data for displaying the Friday hacks in the index page, coreteam members in the `/about` page and coreteam alumni in the `/alumni` page. More details below:

In data, `friday_hacks.yml` is for the Friday hacks (duh!). It contains a list (under `hacks`) of objects each with four fields: `speaker`, `from`, `title` and `venue`. Leave the `speaker` field empty to mark it as 'slot is open', or fill it up if it's filled up. For special occasion such as holidays, delete all fields and put `nohack` as the sole field with the reason as the value, e.g.

```yml
- nohack: Good Friday
```

It also contains a field `start_date` which should be the date-time of the first Friday hack.

`coreteam_members.yml` is for the coreteam member info in `/about`. It contains again a list with objects each with 2 fields: `name` and `description`, so just fill that up. The first guy or gal should be the president.

`alumni.yml` is in the same format as `coreteam_members.yml`. So **to move a coreteam member to alumni, just cut and paste the entry into `alumni.yml`**

## Updating posts

About writing posts: https://gohugo.io/content/

If you are write those generic posts about Friday hacks, please run:

```bash
npm run friday-hacks <Title> <Your name>
```

## Final words

If you dislike any parts of this website, just clone it and push your changes! Make sure you update `README.md`, though, or the octopus will be really pissed off.

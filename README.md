# NUS Hackers Website

This is the repository behind NUS Hackers' website https://nushackers.org, built
with the [Hugo](https://gohugo.io/overview/introduction/) framework.

## Getting started 🚀

To get started, you'll need:

1. [Hugo v0.111.3](https://github.com/gohugoio/Hugo/releases)
2. Yarn v1 with a recent version of NodeJS

Then clone this repository and run

```bash
yarn install # install dependencies
yarn dev # start development server
```

Hugo will now generate the site and watch the directory and update the site when
any changes are made. You can access the site at <http://localhost:1313>.

## Data Management 📊

Most of the data used to populate the site are stored in the `data/` folder as
`.yaml` files. These includes files that contain information about the coreteam
and upcoming projects/events for the semester.

The current academic year and semester are kept tracked of in the `config.toml`
under the `[params]` section. This is used to automatically determine which
project/event data file to use for the current semester. Project/event data
files are named in the format `<project-name>_<academic-year>_<semester>.yml`
and are stored in corresponding `data/<project-name>` folder.

### Coreteam Details 🙋‍♂️🙋‍♀️

Coreteam details and introductions are stored in the
[`/data/coreteam_members.yml`](/data/coreteam_members.yml) file. Include your
wittiest introductions here and don't be shy to share your contact details and
links!

> This file is primarily for active coreteam members, we have a separate file
> for coreteam alumni in [`/data/alumni.yml`](/data/alumni.yml).

### Projects / Events 📅

#### Friday Hacks 🎉

- Data location: [`/data/friday_hacks`](/data/friday_hacks)
- Data Format:
  ```yaml
  start_date: <date-time-of-first-friday-hack>
  start_nr: <number-of-first-friday-hack-in-the-list-below>
  hacks:
     # each event/hack consists of a venue, blog post and talk topics
     - venue: <where>
       blog_post: <blog-post-url>
       topics:
         # each topic consists of a speaker name, affiliation and the title of the talk
         - speaker: <name>
           from: <affiliation>
           title: <title>
      # if there is no friday hack, just put nohack: <reason>
      - nohack: <reason>
  ```
  - ❗️Each hack has a date tagged to it implicitly based on the order of the
    list. The first hack in the list will have `start_date` as the event date,
    the second hack will be the next Friday (`+7d`) and so on.
    - **This means that there needs to be a entry for every Friday between the
      start date and the end of the semester!**
  - `start_date`: This is used to automatically generate the date for each event
    in the list.
  - `start_nr`: This is used to automatically generate the Friday Hacks number
    for each event
    - For example, if `start_nr` is `200`, then the first event in the list
      below is the Friday Hacks #200 and the next event would be Friday Hacks
      #201 and so on (this is all done automatically)
  - Refer to [Creating a Post](#creating-a-post-📝) for more details on how to
    create a new blog post for Friday Hacks

> The data format for Friday Hacks is a little more involved than the others due
> to legacy reasons

#### Hackerschool 📚

- Data location: [`/data/hacker_school`](/data/hacker_school)
- Data Format:
  ```yaml
  events:
    # Each event consists of a topics, venue and date
    - topic: <what-is-the-workshop-about>
      venue: <where>
      date: <when>
  ```
  - _Events are not sorted by date automatically, so do remember to list them in
    chronological order!_

#### Hackers Toolbox 🧰

- Data location: [`/data/hackers_toolbox`](/data/hackers_toolbox)
- Data Format: _same as [Hackerschool](#hackerschool-📚)_

## Creating a Post 📝

All blog posts are stored under the [`content/posts`](/content/post/) folder.

To create a new post:

1. Add a markdown file to the `content/posts` folder
2. Name the file in the format `YYYY-MM-DD-<post-title>.md`
3. Add the following frontmatter to the top of the file:
   ```yaml
   ---
   title: <post-title>
   date: <YYYY-MM-DD>
   url: /<year>/<month>/<day>/<post-tag>
   ```
4. If the post is sponsored, add the following frontmatter:
   ```yaml
   sponsors:
     - <sponsor-name>
   ```

## Adding a new sponsor 🤝

Sponsors will be added to a post via `HTML` partials. These sponsor partials are
stored under the [`layouts/partials/sponsors`](/layouts/partials/sponsors)
folder. The naming convention for these partials is `<sponsor-name>.html`.

To add a new sponsor:

1. Create a new `HTML` partial under the
   [`layouts/partials/sponsors`](/layouts/partials/sponsors/) folder
2. The name of the partial must match the name under the `sponsors` frontmatter
   in the post
3. The logo of the sponsor should be stored under the
   [`static/img/sponsors`](/static/img/sponsors/) folder

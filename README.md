# NUS Hackers website

This is the repository behind NUS Hackers' website https://nushackers.org.

## Requirement

The website is built with Hugo, so if you want to make changes to the templates or structures of the site, please first read about [Hugo](https://gohugo.io/overview/introduction/). But if you are just going to modify the data or update/add a post, you can simply follow the guide below.

## Getting started

You should test the site locally before doing any push. You will need:

1. [Hugo v0.92.0](https://github.com/gohugoio/Hugo/releases)
2. Yarn v1 with a recent version of NodeJS
   - We have stopped using the dated Gulp CSS pipeline that uses node-sass, so the version of NodeJS doesn't matter as much anymore.

Then enter this folder and run

```bash
yarn install
yarn dev
```

Hugo will now generate the site and watch the directory and update the site when any changes are made. You can access the site at <http://localhost:4000>.

## Updating data

First, since Hugo uses [yaml]("http://en.wikipedia.org/wiki/YAML") as the markup for data. It's really simple, so just read about it first.

With some knowledge of yaml, you can take a look at the `content` folder - it contains the data for displaying the Friday hacks in the index page, coreteam members in the `/about` page and coreteam alumni in the `/alumni` page. More details below:

In `data`, `friday_hacks.yml` is for the Friday hacks (duh!). It contains a list (under `hacks`) of objects each with four fields: `speaker`, `from`, `title` and `venue`. Leave the `speaker` field empty to mark it as 'slot is open', or fill it up if it's filled up. For special occasion such as holidays, delete all fields and put `nohack` as the sole field with the reason as the value, e.g.

```yml
- nohack: Good Friday
```

It also contains a field `start_date` which should be the date-time of the first Friday hack.

`coreteam_members.yml` is for the coreteam member info in `/about`. It contains again a list with objects each with 2 fields: `name` and `description`, so just fill that up. The first guy or gal should be the president.

`alumni.yml` is in the same format as `coreteam_members.yml`. So **to move a coreteam member to alumni, just cut and paste the entry into `alumni.yml`**

## Updating posts

About writing posts: https://gohugo.io/content/

If you are write those generic posts about Friday hacks, please use the script  `scripts/gen_fh.py` - yep, it's in Python yay! So install Python and [Pipenv](https://pipenv.readthedocs.io/en/latest/install/) first.

Before running the script for the first time, use Pipenv to install our dependencies.

```bash
$ cd scripts
$ pipenv install
```

To use the script, first make sure you have filled up the Friday hacks entry in `data/friday_hacks.yml`, then just run it.

```bash
$ pipenv run python gen_fh.py
```

It will ask for you name (as the author), and generates the md file in `post/content`. Now go ahead and add in more details to the post.

## Final words

If you dislike any parts of this website, just clone it and push your changes! Make sure you update `README.md`, though, or the octopus will be really pissed off.

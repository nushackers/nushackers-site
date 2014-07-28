nushackers-site
====================

This is the source code of the nushackers blog site http://nushackers.org.

## Requirement

This website is built with jekyll, so if you want to make changes to the templates or structures of the site, please first read about <a href="http://jekyllrb.com">jekyll</a>. But if you are just going to modify the data or update/add a post, you can simply follow the guide below.

## Getting started

It's recommended that you test the site locally before doing any push. To do so, first <a href="https://www.ruby-lang.org/en/installation/">install ruby</a>.

Then, install jekyll:

```bash
$ gem install jekyll
```

Then enter this folder and run

```bash
$ jekyll serve --watch
```

jekyll will now generate the site and watch the directory and update the site when any changes are made. You can access the site at `http://localhost:4000`

## Updating data

First, since jekyll is written in the hipster language ruby, it also uses <a href="http://en.wikipedia.org/wiki/YAML">yaml</a> as the markup for data. It's really simple (and non-mainstream), so just read about it first.

With some knowledge of yaml, you can take a look at the `_data` folder - it contains the data for displaying the Friday hacks in the index page, coreteam memebers in the `/about` page and coreteam alumni in the `/alumni` page. More details below:

`friday_hacks.yml` is for the Friday hacks (duh!). It contains a list (under `hacks`) of objects each with four fields: `speaker`, `from`, `title` and `venue`. Leave the `speaker` field empty to mark it as 'slot is open', or fill it up if it's filled up. For special occasion such as holidays, delete all fields and put `nohack` as the sole field with the reason as the value, e.g. 

```yml
- nohack: Good Friday
```

It also contains a field `start_date` which should be the date-time of the first Friday hack.

`coreteam_members.yml` is for the coreteam member info in `/about`. It contains again a list with objects each with 2 fields: `name` and `description`, so just fill that up. The first guy or gal should be the president.

`alumni.yml` is in the same format as `coreteam_members.yml`. So **to move a coreteam member to alumni, just cut and paste the entry into `alumni.yml`**

## Updating posts

About writing posts: http://jekyllrb.com/docs/posts/

If you are write those generic posts about Friday hacks, please use the script  `_script/gen_fh.py` - yep, it's in Python yay! So install Python first.

To use the script, first make sure you have filled up the Friday hacks entry in `_data/friday_hacks.yml`, then just run it.

```bash
$ cd _scripts
$ python gen_fh.py
```

It will ask for you name (as the author), and generates the md file in `_posts`. Now go ahead and add in more details to the post.

## Final words

If you dislike any part of this website, just clone it and push your change! Make sure you update `READEME.md`, though, or the octopus will be really pissed off.

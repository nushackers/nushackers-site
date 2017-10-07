---
author: Li Kai
categories:
- Digest
date: 2017-09-17T00:00:00Z
published: true
title: 'Digest: NUS Hackers site migration and redesign'
url: /2017/09/17/digest-nus-hackers-site-migration-and-redesign/
---

This summer, the NUS Hackers site went through a huge redesign (you’re looking at it right now). It took the efforts of everyone on the core team to make the blog better. In terms of improvements we managed to improve not only the developer experience but also the speed and performance of the website itself. In this week's digest, we will be talking about some of the improvements we've made and how we've done it.

## Static site generators

Before we dive into the details, let’s take the time to explain what a static site generator is. A static site generator, as the name implies, generates a website. It is static, because once the html files are generated, they will always look and stay the same, which is in contrast to dynamic sites such as Facebook that present different content every time you visit. These generators takes a bunch of content files, normally written in a format called markdown, along with some template HTML files and combine them to make a website. Add in some CSS for styling, and you’ve got a beautiful website. At NUS Hackers, we originally used a generator called [Jekyll](https://jekyllrb.com/). More alternatives can be found at [staticgen](https://staticgen.com).

## Migrating

When the proposal was raised to redesign the site, that idea seemed incredibly difficult because Jekyll, which was written in Ruby, took roughly 11 seconds for a single change to reflect on the browser, which was simply too long and frustrating. As a result, we decided to move to [Hugo](https://gohugo.io).

{{< imglink src="/img/2017/09/hugo.png" alt="gohugo.io" >}}
<br/>

Hugo boasted about its speed and it proved itself when it would take less than a millisecond to rebuild our 500 page blog. it was an astounding change and made developing much easier and convenient.

Hugo also provided a command line tool to migrate from Jekyll to Hugo, which made the migration incredibly easy - `hugo import jekyll` was all it took. However that was not to say that there weren't any difficulties encountered along the way, an easily overlooked feature in Jekyll was that templates could be placed anywhere, even within markdown itself. That was not available in Hugo, and we had to make use of a feature called shortcodes to replace the templates that we had. Shortcodes were simple tags you could write to provide functionality, but they were not as flexible as inlined templates

## Maintainable css

Another feature that was lost was support for [SCSS](http://sass-lang.com/), a superset of CSS, which makes CSS easier to maintain.

<img src="/img/2017/09/scss.png" alt="http://sass-lang.com/"/>

We managed to add it back with a build process which also concurrently spawns the Hugo instance. The build process, written in a javascript library called Gulp, allowed us to work on styling the site where every change would automatically reload the browser to reflect the change. In this build process, we also included libraries Prettier and Stylelint-order, which auto-formatted SCSS. This meant we would never have to worry about how our SCSS code was written, creating stress-free code reviews.

## Faster site & build previews

The last feature that we added was to move our hosting to a service called [Netlify](https://netlify.com).

<img src="/img/2017/09/netlify.png" alt="netlify"/>

Not only did it improve the load time of our site through their incredibly fast Content-Distribution Networks (CDN), they also provided build previews whenever we pushed to GitHub. This meant that any new changes could be previewed in an actual fork of the site. It certainly made reviewing a lot easier and more trustworthy.

All said and done, the new blog is incredibly fast, convenient and sleek. We hope that this digest encouraged you to start your own. Our code is always publicly available at [GitHub](https://github.com/nushackers/nushackers-site)!

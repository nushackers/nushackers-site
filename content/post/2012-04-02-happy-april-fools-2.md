---
author: ejames
categories:
- Chatter
comments: true
date: 2012-04-02T00:00:00Z
title: Happy April Fool's!
url: /2012/04/02/happy-april-fools-2/
---

If you'd visited our site yesterday, you would have seen a command line interface, and a link to a premier Computer Science quiz competition called HackyWin! Here's the email we sent out to the mailing list:

<blockquote>The NUS Hackers are proud to present a premier quiz competition that's targeted at computing students!

<strong>Simply solve 3 questions to win an iPad 3.</strong>

They are guaranteed fun brainteasers, so give them a try. You might be able to solve them and win an iPad 3!

<a href="/hackywin">http://nushackers.org/hackywin</a></blockquote>

We gave three programming questions to people, all of which required solutions that worked under a minute and dealt with <em>all</em> cases to be correct. Here are the questions:

<blockquote><strong>Problem 1: </strong>Dr. Black has been murdered. Detective Jill must determine the murderer, crime scene, and weapon. There are six possible murderers (numbered 1 through 6, Professor Plum to Mrs. Peacock), 10 locations (1 through 10, ballroom to cellar), and six weapons (1 through 6, lead pipe to spanner). Detective Jill tries to guess the correct combination (there are 360 possibilities). Each guess is a theory. She asks her assistant, Jack, to confirm or refute each theory. When Jack refutes a theory, he reports that one of the guesses — murderer, location, or weapon — is wrong. The contestants are tasked with implementing a procedure that plays the role of Detective Jill. A brute-force program that tests all 360 theories earns a mere 50 points. An efficient program that tests no more than 20 theories earns an additional 50.

<strong>Problem 2:</strong> You have bins of capacity <em>V</em>, and n items each of size A<sub>1&le;i&le;n</sub>. Find the minimum number of bins you need such that the total size of items in each bin does not exceed its capacity. Hint: this is a packing problem.

<strong>Problem 3: </strong>You have any number of <em>N</em> points on a table. Your goal is to write a program to connect all of them by lines of minimum total length in such a way that any two points is interconnected by line segments &mdash; either directly, or indirectly via other points and line segments.

If you think about it for a bit, you will realize that the connecting segments do not intersect each other except at the endpoints and thus form a tree.
</blockquote>

This was, of course, and April Fool's joke. When you clicked submit, you were redirected to this <a href="/hackywin/results.html">page</a>, which explained the answers to the 3 problems (2 of which were unsolvable given the constraints).

<blockquote><strong>Solution for Problem 2:</strong> Also known as the Bin Packing problem, this problem is combinatorially NP-hard. That said, optimal solutions to very large instances can be produced with sophisticated algorithms, and non-optimal ones also exist, such as the <strong>first fit algorithm</strong>. Because this question demands an optimal solution <em>for all cases</em>, no solution you provide will be correct given a 1 minute constrain and an arbitrary number of items, each of any size. (Well, if you had access to a supercomputer it might, but that's a tad too much ...) Read more at <a href="https://en.wikipedia.org/wiki/Bin_packing_problem">Wikipedia</a>!

<strong>Solution for Problem 3:</strong> This problem, also known as the <a href="https://en.wikipedia.org/wiki/Steiner_tree_problem">Steiner tree problem</a>, is NP-hard for general <em>N</em> (which is exactly what this question was asking for)! In fact, an expression of this problem was among Karp's <strong>original 21 NP-complete problems</strong>. As an interesting aside, computer science folklore has long held that soap film, applied to a series of glass plates may solve this problem where computers may not. <a href="http://www.tjhsst.edu/~rlatimer/techlab06/Students/OuyangPaper06F.pdf">See this paper for more</a>.</blockquote>

We hope that you've spent some time thinking about Computer Science problems you might not have otherwise known of, and ...

<strong>Happy April Fool's!</strong>

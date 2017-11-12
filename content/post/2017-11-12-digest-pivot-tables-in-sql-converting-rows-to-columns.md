---
author: Herbert Ilhan Tanujaya
categories:
  - Digest
date: 2017-11-12T00:00:00.000Z
title: "Digest: Pivot Tables in SQL - Converting Rows to Columns"
tags:
  - SQL
  - pivot tables
url: /2017/11/digest-pivot-tables-in-sql-converting-rows-to-columns
aliases:
  - /2017/11/12/digest-pivot-tables-in-sql-converting-rows-to-columns
---

A few weeks ago I gave a talk at NUS Hackers's Friday Hacks on some advanced
tips in using SQL. (It was my first technical talk, btw!) Here, I will give one
of those tips in more detail.

## The Background

I have been working on a website that hosts math olympiad contests monthly.
(Shameless plug - source code at https://github.com/donjar/kontes-terbuka,
website at https://ktom.tomi.or.id. Even though it is in Bahasa Indonesia,
Google Translate gives a good enough translation.) In each contest, there are
several structured questions that a contestant can solve.  The schema is
something like this:

Submissions:
- id: primary key
- user_id: foreign key to users
- problem_id: foreign key to problems
- score: integer

(There are some sample SQL data that can be found
[here](https://github.com/donjar/sql-wizardry). The file `dump.sql` is of your
interest; check out the `contest_scores` table. The file
`contest_pivot_table.sql` is the solution to the problem below. This repo was
originally made for my SQL Wizardry presentation.)

## The Problem

Let's say the current data looks like this:
```
 id | user_id | problem_id | score
----+---------+------------+-------
  1 |       1 |          1 |     3
  2 |       1 |          2 |     8
  3 |       1 |          3 |     1
  4 |       2 |          1 |     7
  5 |       2 |          2 |     3
  6 |       2 |          3 |     3
  7 |       3 |          1 |     4
  8 |       3 |          2 |     2
  9 |       3 |          3 |     3
 10 |       4 |          1 |     7
 11 |       4 |          2 |     5
 12 |       5 |          1 |     4
 13 |       5 |          3 |     7
 14 |       6 |          2 |     3
 15 |       6 |          3 |     4
 16 |       7 |          1 |     4
 17 |       7 |          2 |     4
 18 |       7 |          3 |     9
 19 |       8 |          1 |     7
 20 |       8 |          2 |     2
 21 |       8 |          3 |     4
 22 |       9 |          1 |     8
 23 |       9 |          2 |     0
 24 |       9 |          3 |     4
 25 |      10 |          1 |     3
 26 |      10 |          2 |     3
 27 |      10 |          3 |     6
```

Obviously data like this is not suitable to be shown to the end user. What we
want is something like this:
```
 user_id | problem_1 | problem_2 | problem_3
---------+-----------+-----------+-----------
       1 |         3 |         8 |         1
       2 |         7 |         3 |         3
       3 |         4 |         2 |         3
       4 |         7 |         5 |
       5 |         4 |           |         7
       6 |           |         3 |         4
       7 |         4 |         4 |         9
       8 |         7 |         2 |         4
       9 |         8 |         0 |         4
      10 |         3 |         3 |         6
```

Notice that this involves converting rows of the table into columns: in this
case, the `problem_id` needs to be "split" into `problem_1`, `problem_2`, and
`problem_3`.

You can't do this in a normal SQL SELECT statement! Normally, when you select
columns, you can only select based on operations on the existing columns. There
are no operations that allow you to convert rows into columns like this way.

You can work around this with table joins though, for example:
```sql
WITH (
  SELECT
    user_id,
    problem_1 AS score
  FROM submissions
  WHERE
    problem_id = 1
) AS problem_1_table, (
  SELECT
    user_id,
    problem_2 AS score
  FROM submissions
  WHERE
    problem_id = 2
) AS problem_2_table, (
  SELECT
    user_id,
    problem_3 AS score
  FROM submissions
  WHERE
    problem_id = 3
) AS problem_3_table

SELECT
  problem_1_table.user_id,
  problem_1,
  problem_2,
  problem_3
FROM problem_1_table
FULL OUTER JOIN problem_2_table
ON problem_1_table.user_id = problem_2_table.user_id
FULL OUTER JOIN problem_3_table
ON problem_1_table.user_id = problem_3_table.user_id
```

Basically, `problem_1_table` is a table that contains the (`user_id`, `score`)
pair for submissions with `problem_id = 1`, and so on. Afterwards, we join them
on the `user_id` to produce the table we want.

In fact, this was our original approach to the problem! The website was built
with Ruby on Rails, and we used a loop in Ruby to loop through all problems and
generate the corresponding SQL query. I would see SQL queries like this often:

```sql
  SELECT user_contests.*, marks.short_mark, marks.long_mark, marks.total_mark, case when marks.total_mark >= gold_cutoff then 'Emas' when marks.total_mark >= silver_cutoff then 'Perak' when marks.total_mark >= bronze_cutoff then 'Perunggu' else '' end as award, "long_problem_marks_269"."problem_no_269", "long_problem_marks_271"."problem_no_271", "long_problem_marks_270"."problem_no_270", "long_problem_marks_268"."problem_no_268", RANK() OVER(ORDER BY marks.total_mark DESC) AS rank FROM "user_contests" INNER JOIN "contests" ON "contests"."id" = "user_contests"."contest_id" INNER JOIN "users" ON "users"."id" = "user_contests"."user_id" INNER JOIN (SELECT user_contests.*, short_marks.short_mark, long_marks.long_mark, (short_marks.short_mark + long_marks.long_mark) as total_mark FROM "user_contests" INNER JOIN (SELECT user_contests.id as id, sum(case when short_submissions.answer = short_problems.answer then 1 else 0 end) as short_mark FROM "user_contests" LEFT OUTER JOIN "short_submissions" ON "short_submissions"."user_contest_id" = "user_contests"."id" LEFT OUTER JOIN "short_submissions" "short_submissions_user_contests_join" ON "short_submissions_user_contests_join"."user_contest_id" = "user_contests"."id" LEFT OUTER JOIN "short_problems" ON "short_problems"."id" = "short_submissions_user_contests_join"."short_problem_id" WHERE "user_contests"."contest_id" = 29 AND ("short_submissions"."short_problem_id" = "short_problems"."id" OR ("short_submissions"."short_problem_id" IS NULL AND "short_problems"."id" IS NULL)) GROUP BY "user_contests"."id") short_marks ON "user_contests"."id" = "short_marks"."id" INNER JOIN (SELECT user_contests.id as id, sum(coalesce(long_submissions.score, 0)) as long_mark FROM "user_contests" LEFT OUTER JOIN "long_submissions" ON "long_submissions"."user_contest_id" = "user_contests"."id" WHERE "user_contests"."contest_id" = 29 GROUP BY "user_contests"."id") long_marks ON "user_contests"."id" = "long_marks"."id" WHERE "user_contests"."contest_id" = 29) marks ON "user_contests"."id" = "marks"."id" LEFT OUTER JOIN (SELECT user_contests.id as id, long_submissions.score as problem_no_269 FROM "user_contests" LEFT OUTER JOIN "long_submissions" ON "long_submissions"."user_contest_id" = "user_contests"."id" WHERE "long_submissions"."long_problem_id" = 269) long_problem_marks_269 ON "user_contests"."id" = "long_problem_marks_269"."id" LEFT OUTER JOIN (SELECT user_contests.id as id, long_submissions.score as problem_no_271 FROM "user_contests" LEFT OUTER JOIN "long_submissions" ON "long_submissions"."user_contest_id" = "user_contests"."id" WHERE "long_submissions"."long_problem_id" = 271) long_problem_marks_271 ON "user_contests"."id" = "long_problem_marks_271"."id" LEFT OUTER JOIN (SELECT user_contests.id as id, long_submissions.score as problem_no_270 FROM "user_contests" LEFT OUTER JOIN "long_submissions" ON "long_submissions"."user_contest_id" = "user_contests"."id" WHERE "long_submissions"."long_problem_id" = 270) long_problem_marks_270 ON "user_contests"."id" = "long_problem_marks_270"."id" LEFT OUTER JOIN (SELECT user_contests.id as id, long_submissions.score as problem_no_268 FROM "user_contests" LEFT OUTER JOIN "long_submissions" ON "long_submissions"."user_contest_id" = "user_contests"."id" WHERE "long_submissions"."long_problem_id" = 268) long_problem_marks_268 ON "user_contests"."id" = "long_problem_marks_268"."id" WHERE "user_contests"."contest_id" = 29 AND "users"."province_id" = 35  ORDER BY "marks"."total_mark" DESC
```

It wasn't very pretty Ruby and SQL code, but hey, it works. But of course, this
does not sit really well with me - using Ruby to generate SQL and using that
generated code to query data seems weird, isn't it?

Of course we can just select all data in SQL and do the processing in Ruby on
Rails. However, as the saying goes - do the data processing in the database
level, where it is suitable for the job right?

Enter pivot tables.

## Pivot Tables

You might heard pivot tables from Microsoft Excel. To quote Wikipedia:

> A pivot table is a table that summarizes data in another table, and is made
> by applying an operation such as sorting, averaging, or summing to data in
> the first table, typically including grouping of the data.

The "grouping of the data" is of interest here.

### Caveat

Pivot tables have different implementations across different databases. I am
only going to discuss how to do it on PostgreSQL, as that is the database I am
using in my application. You should be able to find implementations for other
databases by searching, for example, "pivot tables MySQL".

### Crosstab

In PostgreSQL, the relevant function is called "crosstab". It is available as
an extension, and hence, you should install it first by running `CREATE
EXTENSION tablefunc;` as a superuser.

The relevant documentation can be found
[here](https://www.postgresql.org/docs/10/static/tablefunc.html). One thing you
might notice, though, is that there are actually four different crosstab
functions!

The functions are actually generating pivot tables, only with different
abstraction levels. I found that the `crosstab(text source_sql,
text category_sql)` function produces the result I needed. To quote the
documentation:

> `source_sql` is a SQL statement that produces the source set of data. This
> statement must return one `row_name` column, one category column, and one
> value column. It may also have one or more "extra" columns. The `row_name`
> column must be first. The category and value columns must be the last two
> columns, in that order. Any columns between `row_name` and category are
> treated as "extra". The "extra" columns are expected to be the same for all
> rows with the same `row_name` value.

So basically, `source_sql` is in the form:
```sql
SELECT key(s), categories, values FROM ...
```
and the `category_sql` matches the values that we want in the category to
separate.

An example will make these concepts clearer. Going to the example we discussed
previously, we notice that the key is the `user_id` - basically, this is the
column we want to be at the first column. The category is `problem_id`, since
this is what we want the next columns of the resulting pivot table to be. And
finally, the values to be filled in inside the resulting table would be `score`.
It is normal to use an `ORDER BY key` as well here, so that the resulting pivot
table is not jumbled. Combining all of them, we have this `source_sql` query:
```
SELECT user_id, problem_id, score FROM submissions ORDER BY user_id
```

For the category, we know that the problem IDs we want is 1, 2, 3, and hence,
the corresponding `category_sql` is:
```
SELECT 1, 2, 3
```
(in reality we would want something like `SELECT id FROM problems ORDER BY id`).

And at the end, we would need to specify the columns to be generated as well,
with this format:
```
("column1" category1, "column2" category2, ...)
```

In this case, it would be:
```
("user_id" int, "problem_1" int, "problem_2" int, "problem_3" int)
```

Hence, the resulting SQL query is:
```
SELECT * FROM crosstab(
  'SELECT user_id, problem_id, score FROM submissions ORDER BY user_id',
  'SELECT 1, 2, 3'
) AS (
  "user_id" int,
  "problem_1" int,
  "problem_2" int,
  "problem_3" int
)
```

This will return just what we wanted!

## Problems

While this query is "cleaner" than the SQL joins "workaround" I wrote
previously, there are still some problems with this solution. Firstly, there
is a need to specify the columns in the resulting pivot table. While this can
also be generated with the underlying framework (with Ruby etc.), we still need
to query two times: once to get the column definitions (for example, `SELECT
id FROM problems`), and once to do the actual crosstab query. If I remember
correctly, this problem is not specific to PostgreSQL; other databases also have
this problem. This solution will not solve the problem of using the application
to craft SQL queries.

The other problem which might not be obvious is about ORMs - it is highly
unlikely that ORMs have support for pivot tables. This may cause problems with
using ORM tools - for example, while ActiveRecord (the ORM in Ruby on Rails)
has a `find_by_sql` method, chaining it with another ActiveRecord method can
cause bugs. In my case, `Submissions.find_by_sql(crosstab_query).count` does
not work (as I assume Rails doesn't know where to put the `COUNT` query).

With two queries running, performance might also be a problem. From my
observations, the SQL joins query takes around 70 ms, while these two queries
take around 50 ms in total; however, this does not account network overheads
etc. A more systematic benchmarking is needed to confirm if this solution is
indeed faster than the joining solution.

## Conclusion

If you need to somehow convert rows into columns, and vice versa, to do
grouping/aggregation, pivot tables might be for you. While several problems
exist, I still believe that pivot table is the right tool for the job and the
resulting solution is "cleaner".

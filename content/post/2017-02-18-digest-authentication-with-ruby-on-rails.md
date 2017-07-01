---
author: Herbert Ilhan Tanujaya
categories:
- Digest
date: 2017-02-18T00:00:00Z
title: 'Digest: Authentication with Ruby on Rails'
url: /2017/02/18/digest-authentication-with-ruby-on-rails/
---

## Introduction
Nowadays, nearly all websites have an authentication system in place, using
usernames and passwords. In this article, we will create a simple authentication
in Ruby on Rails, a popular web application framework. This article is mainly
aimed at those who are just getting started with their first web application
(but have some knowledge of Rails).

When I first learned Rails and web development in general, I wanted to create
a website for my organization. One requirement for the website was to have an
authentication system, so I searched for Ruby gems that could help with this.
One of the most popular gems is [devise](https://github.com/plataformatec/devise).
However, this gem is not recommended for beginners to Rails
[as mentioned in the README](https://github.com/plataformatec/devise#starting-with-rails)!

Based on my experiences, this article will walk through the steps needed to
create a sufficiently secure authentication system in Ruby on Rails 5.0.1 on
Ruby 2.4.0.

## What to store in database?
It is totally not advisable to store plain passwords in the database. For one,
developers can see the password you store, which is already a security breach.
An even more important reason, though, is to limit the damage when your database
is compromised. Imagine if you store plain passwords in the database and your
database is stolen by hackers - now the hackers are able to compromise all
accounts in your system easily. Now imagine if you store them in a secure format
such that even if the hackers steal your database, they still can't get the
passwords easily - less damage would be done that way.

To achieve this, we will hash the passwords in the database. Basically, what
this means is that we will use a
[hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function) that
takes your passwords as an input and gives out a (seemingly) random string of
a certain length. There are some properties that make certain functions suitable
as a hash function:
- it has finite output possibilites (since it has a fixed length); however, it
is almost impossible to find two inputs that hash to the same output
- computing the hash is quick and deterministic (meaning that hashing the same
input always produces the same output)
- given a hash, it is nearly impossible to find an input that hashes into it
- a small change to the input makes a big change in the output

For our purposes, we will be using [BCrypt](https://en.wikipedia.org/wiki/Bcrypt)
that is conviniently bundled already in Ruby on Rails.

There is another problem though - if we only store the password hash, an
attacker can compute as many hashes as they can, and store it in some table.
When the database is compromised, the attacker can just use this table to
lookup inputs that hash to these passwords! This attack is called
[rainbow tables](https://en.wikipedia.org/wiki/Rainbow_table).

Hence, we need to "upgrade" our hashing system by including
[password salts](https://en.wikipedia.org/wiki/Salt_(cryptography)).
Essentially, this means our hashes depend not only on our initial passwords, but
also on the randomly generated salts. Each salt is associated with a user in
our system and every user should have different salts, so that precomputing
the hashes would take much more time (since the attacker also needs to use
various salts as well).

Hence, in our database, we will store three things:
1. Username - string, not null, must be unique
2. Password hash - string, not null
3. Password salt - string, not null

So much about security. Let's get to work!

## Creating our application
Let's create our app! Assuming you have installed Rails
([check this out](http://installfest.railsbridge.org/installfest/) if you
haven't), in your project root, run `rails new simple-auth` (here `simple-auth`
is the name of my app). After the installation is done, enter your app folder.

Now, let's generate the models we need for the application. To do so, run:
`bin/rails g model User username:string password_hash:string password_salt:string`

Check the migration file generated (in `db/migrate` folder). Let's add not null
and unique constraints on the database by changing the migration file into:
```
class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users do |t|
      t.string :username, null: false, unique: true
      t.string :password_hash, null: false
      t.string :password_salt, null: false

      t.timestamps
    end
  end
end
```
Afterwards, run `bin/rails db:migrate` to migrate the database.

Next, enable the BCrypt gem by uncommenting the corresponding line in the
Gemfile: `# gem 'bcrypt', '~> 3.1.7'`. Run `bundle install` afterwards
(or just `bundle`).

Now, in your User model, add these lines:
```
class User < ApplicationRecord
  attr_accessor :password
  validates :username, presence: true, uniqueness: true
  validates :password, presence: true, on: :create

  before_validation(on: :create) do
    encrypt_password
  end

  def authenticate(password)
    password_hash == BCrypt::Engine.hash_secret(password, password_salt)
  end

  private

  def encrypt_password
    self.password_salt = BCrypt::Engine.generate_salt
    self.password_hash = BCrypt::Engine.hash_secret(password, password_salt)
  end
end
```

Here's some explanation:
- `attr_accessor :password` adds a "password" field in your User model that is
not saved into the database.
- The next two lines validate both username and password, by making sure they
exist. Username is also ensured to be unique. Now you might realize that the
username is already guaranteed in the database to be not null and unique; why
bother doing it again in the model? Actually, it is enough to have it in either
the model or the database (assuming the database only interacts with this app).
I'm just going to including it in both.
- The `before_validation` block makes sure that the password is encrypted
before creating.
- The `authenticate` method provides a method in the user to check if the given
password (as argument) is the user's correct password.
- The `encrypt_password` method generates the salt and the hash. It is set
private because there is no need to expose this method.

Now that we've done this, let's open the console by using `bin/rails c`.

Let's create a user! For example, I'll create a user named `donjar` with
password `NUSh4ck3r5`. Run in irb:
`u = User.create(username: 'donjar', password: 'NUSh4ck3r5')`

The user should now be saved into the database. If you run `User.all` it should
show your user, along with its hash and salt. Here's what happened in my
computer:
`#<ActiveRecord::Relation [#<User id: 1, username: "donjar", password_hash: "$2a$10$xb9MMJaEm7aP.lKdIPG0aeH/etrXqE4A/ObLri/8IMT...", password_salt: "$2a$10$xb9MMJaEm7aP.lKdIPG0ae", created_at: "2017-02-16 15:03:23", updated_at: "2017-02-16 15:03:23">]>`

This can be different from the user in your computer - it's okay! In fact, this
shows that the salt is randomly generated, and with the same password yet a
different salt, the hash will be very different.

Now we can test authenticating our user:
```
> u.authenticate('NUSh4ck3r5')
=> true
> u.authenticate('NUShackers')
=> false
> u.authenticate('nush4ck3r5')
=> false
```
So this means our user system is working. Yay!

## What's next?
For a simple authentication system that is only working in the model, this is
sufficient. However, if you are going to create a full application with view
and controller, you also need to add the login and logout functions, which
need more than this. There are many tutorials online - we might even add one
in the future!

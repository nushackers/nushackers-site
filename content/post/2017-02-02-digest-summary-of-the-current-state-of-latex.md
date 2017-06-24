---
author: Johannes Choo
categories:
- Digest
date: 2017-02-02T00:00:00Z
title: 'Digest: Summary of the Current State of LaTeX'
url: /2017/02/02/digest-summary-of-the-current-state-of-latex/
---

This article will be structured in two parts. The first discusses
reasons to use or not use LaTeX to typeset your document, while the second
discusses the current landscape of TeX engines,
document typesetting systems, and distributions.

## 1. Introduction: do you really need to use TeX?

Back in its early days, the TeX typesetting system may have been the
premier typesetting solution. This is no longer true for many use
cases. Popular, commercial typesetting systems have matured
considerably over the last decade. Word 2007 incorporated native
equation composition which markup is actually more semantically
expressive than TeX's, and Word 2010 incorporated support for
ligatures. Barring mathematical typesetting, I believe (but cannot
testify) that solutions offered by Adobe (especially InDesign) and
Apple come close to, or surpass, the TeX system. In addition,
the [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) nature of most of
these solutions' UX lend them a
tighter
[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).

What redeeming qualities, then, does typesetting in the TeX system
offer? To me, there are three app-killers; one is the ability to make
document-global edits through two mechanisms: TeX macros, and good ol'
search-and-replace. These features, lacking in affordable WYSIWYG
editors, allow us to replace a fallible hunt-and-peck editing
operation with a quick, straightforward one. The other is the number
of packages that facilitate typesetting many non-conventional texts.
The last, of course, is that it is free.

### Macros

It is not infrequent, during the composition of a document, that you
find it necessary to change the appearance or treatment of a certain
class of text, say the placement of floats or bullets of a list. As
far as I know, outside of theming, Word does not offer a reliable
mechanism to perform such document-wide changes reliably, and I am
uncertain, but skeptical, about other commercial WYSIWYG solutions.

A TeX system, on the other hand, allows us to define macros that
specify markup, and define them in the document preamble, hence
localizing markup. TeX macros offer another advantage: they allow us
to specify semantic markup for (document-local) classes of text rather
than having to resign ourselves to presentation markup. By semantic
markup for document-local classes of text, I mean notions that are not
universal in all documents that need to be typeset and hence are not
offered in WYSIWTG systems. Examples include conjugation tables
template for language books, theorem environments, the first
occurrence of new jargon in a textbook, todo placeholders to indicate
further writing/editing needed, etc. Tne advantage of semantic markup
is that we can easily change the presentation of these classes fromj
one location, and that we can easily extract such classes of text for
other purposes (e.g. creating flashcards from jargon introduced in a
textbook)

### Visible markup

The other mechanism is its amenability to search-and-replace
operations. Where we want to make changes on some but not necessarily
all markup that fit a pattern, we can easily create a regex for it
(though not foolproof, since regex, being regular, has trouble with
context-free notions). This is not possible in WYSIWYG documents,
since much presentation markup is hidden behind menus and not directly
editable as text, and since there is the occasional piece of text that
appears the same but has a different markup.

Macros and visible markup taken together mean that it is far easier to
ensure consistency in a LaTeX-typeset document than one from a WYSIWYG
editor.

### Packages and versatility

TeX was born in academia, and the packages in a typical TeX
distribution reflects that. There are packages that provides theorem
environments for mathematicians. There are packages for typesetting
editions of ancient manuscripts. There are packages that enable more
creatively typeset passages required by some genres of poetry. There
are packages that allow one to typeset a deluge of footnotes as a
paragraph, which is often found in critical editions of literature.
There are packages for typesetting code listings and for pseudocode.
Hence if your document requires unusual typesetting that nevertheless
is already popular and conventional among a group of specialists,
chances are you'll find a package for that.

After weighing the pros and cons, if you are still interested in
typesetting a document in LaTeX, and are interested in producing a
document beyond the generic
[Computer Modern](https://en.wikipedia.org/wiki/Computer_Modern) look,
read on.

## 2. Engines, Document Preparation Systems, Distributions

### Beyond TeX and pdfTeX, the XeTeX and LuaTeX engines.

#### pdfTeX

The TeX program by Knunth, while stable and complete, nevertheless was
born too early and misses out on three important developments in
digital typesetting: the PDF format, and OpenType. The output of TeX
is a DVI file, which while convertible to a PostScript or PDF file,
lacks PDF features like PDF hyperlinking, PDF forms, and PDF table of
contents, etc.

To remedy this (and introduce a couple other features), pdfTeX was
born, that primarily compiled directly to PDF files.

#### XeTeX

Nevertheless, neither TeX nor pdfTeX support newer font technologies
such as TrueType and OpenType. Among others, TrueType and OpenType
formats allow font distributors a standardized way to specify and
provide support for many typographic features; specifying different
features for different languages and scripts, support for small caps,
superscripts, subscripts, lining figures, old-style figures,
proportional figures, ligatures, optional ligatures, combining
accents, contextual alternatives, etc., all in a single,
customer-friendly font file. Hence typographers have embraced
OpenType. My favorite examples of the versatility of OpenType comes
from
[Kazuraki](http://www.imug.org/presentations/imug-lunde-09162010.pdf)
and
[Zapfino Arabic](http://ilovetypography.com/2015/02/22/making-arabic-fonts-climbing-everest/).

The XeTeX engine introduced compatibility with OpenType fonts.

#### LuaTeX

Current development, however, is focused on LuaTeX. As the name
suggests, LuaTeX is an engine that exposes Lua bindings. It is also
designed to be compatible with XeTeX documents, supporting OpenType as
well, though having different internals.

The TeX program, along with its macro language, was invented before
the benefits of proper encapsulation in structured programming and in
object-oriented programming were widespread and accepted. In addition,
TeX lacks first-class support for numerical computation. All these
legacy decisions mean that writing involved macros and macro packages
often involve a fair number of kludges and side cases, arcane,
non-obvious code, and non-obvious incompatibilities with other
packages. LuaTeX is a step towards alleviating this situation, along
with LaTeX3 (though the latter's pace of development makes Perl 6 look
like the Road Runner.)

In between, there have been other TeX-like engines being developed
such as NTS, ExTeX, Omega and Aleph, though their functionality have
been largely superseded by newer engines.

### TeX, LaTeX and ConTeXt

Documents compiled by any one of the above engines can be said to be
TeX, LaTeX, or ConTeXt documents. TeX documents have to specify
themselves the presentation of their elements somewhere. LaTeX is a
macro framework sitting on top of TeX that specifies sane defaults,
guided by an objective of allowing the author to care as little about
the presentation of their document if desired; LaTeX documents assume
that they will be compiled along with the LaTeX. As a result, it is
not always straightforward to change certain aspects of a LaTeX
document. ConTeXt is another macro framework incompatible with LaTeX,
but ConTeXt is far more customization-friendly out of the box. The
latest version of ConTeXt supports only LuaTeX, utilizing its modern
feature set. Both LaTeX and ConTeXt specify mechanisms to import
third-party packages. Ultimately, however, for better or worse, LaTeX,
perhaps by virtue of being more accessible than TeX and of having been
started earlier than ConTeXt, is the target of most third-pary
packages being distributed freely.

### TeX Live

Whereas there used to be a variety of TeX distributions, TeX Live for
Linux and Windows and its twin MacTeX have emerged to be the superior,
albeit slightly weighty, standard distribution. They are maintained by
the TeX Users Group and come with utilities to regularly update or
auto-update from the CTAN (Comprehensive Tex Archive Network) mirrors.
Being somewhat of a niche piece of software, CTAN packages do not
often update as frequently as those in repositories for OSes,
popular programming languages, etc.

## Ending Note

I hope this clarifies for the reader what the words and differences
between TeX, LaTeX, ConTeXt, pdfTeX, XeTeX, LuaTeX, CTAN, etc. are,
and gives an insight into the development history of the TeX
ecosystem. If TeX is right for you, I encourage you to try out the
newer engines and try out some novel customizations. To that end, I am
writing a companion post which is an annotation of a template that I
base my documents off.

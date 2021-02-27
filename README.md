# Perl 🐫 `map` versus Python 🐍 `dict` Comprehension

Perl’s `map` function always returns lists, even when the intent to create a
hash is abundantly clear. This leads to CPU cycles wasted on creating the hash
from the list after-the-fact.

Python’s `dict` comprehension directly constructs a dictionary, the Python
equivalent to a Perl hash, on the fly, without forcing an intermediate `list`
stage.

## Results

### tl;dr

Python wins by taking about half the time Perl takes.

### Stats for Nerds

Data to be collected.

## Why?

[This Twitter thread](https://twitter.com/grhmc/status/1365462790425751552 "by
Graham Christensen") sparked a discussion leading to this benchmarking code
being written.

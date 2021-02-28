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

#### Perl

|||
|-|-|
| Regular Hash            | 0.452912092208862s |
| Keys Assignment         | 0.452517986297607s |
| Numeric Regular Hash    | 2.83940291404724s  |
| Numeric Keys Assignment | 2.83703708648682s  |
| Numeric No Hash         | 0.647165060043335s |

#### Python

|||
|-|-|
| Regular Hash         | 0.23767730799954734s |
| Numeric Regular Hash | 0.8262694709992502s  |

## Why?

[This Twitter thread](https://twitter.com/grhmc/status/1365462790425751552 "by
Graham Christensen") sparked a discussion leading to this benchmarking code
being written.

## How?

```sh
git clone https://gitlab.com/ankitpati/pl-map-vs-py-dcomp.git
cd pl-map-vs-py-dcomp/
./run.sh
```

For tweaking things, consult the source!

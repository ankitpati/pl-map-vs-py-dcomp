# Perl 🐪 `map` versus Python 🐍 `dict` Comprehension

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

| Test                    | Time Taken (s)    |
|-------------------------|-------------------|
| Regular Hash            | 0.452912092208862 |
| Keys Assignment         | 0.452517986297607 |
| Numeric Regular Hash    | 2.83940291404724  |
| Numeric Keys Assignment | 2.83703708648682  |
| Numeric No Hash         | 0.647165060043335 |

#### Python

| Test                 | Time Taken (s)      |
|----------------------|---------------------|
| Regular Hash         | 0.23767730799954734 |
| Numeric Regular Hash | 0.8262694709992502  |

#### Perl with Loops (not `map`)

| Test                    | Time Taken (s)    |
|-------------------------|-------------------|
| Regular Hash            | 0.336189031600952 |
| Keys Assignment         | 0.339548110961914 |
| Numeric Regular Hash    | 1.44092202186584  |
| Numeric Keys Assignment | 1.47567176818848  |

#### PyPy

| Test                 | Time Taken (s)      |
|----------------------|---------------------|
| Regular Hash         | 0.06730515199888032 |
| Numeric Regular Hash | 0.30881453300025896 |

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

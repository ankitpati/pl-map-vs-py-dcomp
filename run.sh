#!/usr/bin/env bash

me="$(basename "$0")"
mydir="$(dirname "$0")/"

test "$#" -ne 0 && echo "Usage: $me" && exit 1

ITERATIONS=10000
BMARK_OPTS=("$mydir/data/"{raw,{,numeric_}processed}_data.csv "$ITERATIONS")

echo 'CPython'
"$mydir/src/bmark.py" "${BMARK_OPTS[@]}"
echo
echo 'PyPy'
pypy3 "$mydir/src/bmark.py" "${BMARK_OPTS[@]}"
echo
echo 'Perl'
"$mydir/src/bmark.pl" "${BMARK_OPTS[@]}"
echo
echo 'Perl with Loops (not `map`)'
"$mydir/src/bmark-loops.pl" "${BMARK_OPTS[@]}"

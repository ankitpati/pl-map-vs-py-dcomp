#!/usr/bin/env bash

me="$(basename "$0")"
mydir="$(dirname "$0")/"

test "$#" -ne 0 && echo "Usage: $me" && exit 1

ITERATIONS=10000
BMARK_OPTS=("$mydir/data/"{raw,{,numeric_}processed}_data.csv "$ITERATIONS")

"$mydir/src/bmark.py" "${BMARK_OPTS[@]}"
"$mydir/src/bmark.pl" "${BMARK_OPTS[@]}"

#!/usr/bin/env perl

use strict;
use warnings;

use Benchmark qw(:hireswallclock timeit);

sub benchmark {
    my %processed = map { $_ => $_ * $_ } 0..1000;
    return %processed;
}

# Total, wallclock time for lots of runs.
print ((timeit 10000, \&benchmark)->real, "\n");

# Verify correctness, and compare with other benchmarked code.
my %ret = benchmark;
print "$_,$ret{$_}\n" foreach sort { $a <=> $b } keys %ret;

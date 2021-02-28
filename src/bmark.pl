#!/usr/bin/env perl

use strict;
use warnings;
use autodie;

use Text::CSV;
use Benchmark qw(:hireswallclock timeit);
use Test::More tests => 5;

my @raw_data;
my %processed_data;
my %numeric_processed_data;

sub regular_hash {
    my %processed = map {
        $_->[0] => $_->[3] && $_->[2] ? ($_->[3] - $_->[2]) / $_->[1] : undef;
    } @raw_data;
    return %processed;
}

sub keys_assignment {
    my %processed;

    keys %processed = 128;

    %processed = map {
        $_->[0] => $_->[3] && $_->[2] ? ($_->[3] - $_->[2]) / $_->[1] : undef;
    } @raw_data;
    return %processed;
}

sub numeric_regular_hash {
    my %processed = map { $_ => $_ * $_ } 0 .. 1000;
    return %processed;
}

sub numeric_keys_assignment {
    my %processed;
    keys %processed = 1001;
    %processed = map { $_ => $_ * $_ } 0 .. 1000;
    return %processed;
}

sub numeric_no_hash {
    return map { $_ => $_ * $_ } 0 .. 1000;
}

sub main {
    my $reader = Text::CSV->new;

    open my $raw_data_csv, '<', $ARGV[0];
    @raw_data = @{ $reader->getline_all ($raw_data_csv) };
    close $raw_data_csv;

    open my $processed_data_csv, '<', $ARGV[1];
    %processed_data = map { $_->[0] => $_->[1] eq 'N/A' ? undef : $_->[1] }
      @{ $reader->getline_all ($processed_data_csv) };
    close $processed_data_csv;

    open my $numeric_processed_data_csv, '<', $ARGV[2];
    %numeric_processed_data =
      map { @$_ } @{ $reader->getline_all ($numeric_processed_data_csv) };
    close $numeric_processed_data_csv;

    my $timed_iteration = $ARGV[3];

    # Total, wallclock time for lots of runs.
    diag
      "Regular Hash:\t\t\t",
      (timeit $timed_iteration, \&regular_hash)->real, "s\n",
      "Keys Assignment:\t\t",
      (timeit $timed_iteration, \&keys_assignment)->real, "s\n",
      "Numeric Regular Hash:\t\t",
      (timeit $timed_iteration, \&numeric_regular_hash)->real, "s\n",
      "Numeric Keys Assignment:\t",
      (timeit $timed_iteration, \&numeric_keys_assignment)->real, "s\n",
      "Numeric No Hash:\t\t",
      (timeit $timed_iteration, \&numeric_no_hash)->real, "s\n",
      ;

    # Verify correctness, and compare with other benchmarked code.
    my %regular_hash_ret            = regular_hash;
    my %keys_assignment_ret         = keys_assignment;
    my %numeric_regular_hash_ret    = numeric_regular_hash;
    my %numeric_keys_assignment_ret = numeric_keys_assignment;
    my %numeric_no_hash_ret         = numeric_no_hash;

    while (my ($key, $value) = each %regular_hash_ret) {
        $regular_hash_ret{$key} = $value ? sprintf '%.7f', $value : $value;
    }

    while (my ($key, $value) = each %keys_assignment_ret) {
        $keys_assignment_ret{$key} = $value ? sprintf '%.7f', $value : $value;
    }

    is_deeply \%regular_hash_ret, \%processed_data, 'Regular Hash is correct';
    is_deeply \%keys_assignment_ret, \%processed_data,
      'Keys Assignment Hash is correct';
    is_deeply \%numeric_regular_hash_ret, \%numeric_processed_data,
      'Numeric Regular Hash is correct';
    is_deeply \%numeric_keys_assignment_ret, \%numeric_processed_data,
      'Numeric Keys Assignment Hash is correct';
    is_deeply \%numeric_no_hash_ret, \%numeric_processed_data,
      'Numeric No Hash is correct';

    return;
}

main unless caller;

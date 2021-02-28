#!/usr/bin/env python
'''Benchmark Runner'''

from sys import argv
from csv import reader
from timeit import timeit
from unittest import TestCase, TestSuite, TextTestRunner

raw_data = []
processed_data = dict()
numeric_processed_data = dict()


def regular_hash():
    '''Code being benchmarked'''
    processed = {x[0]: (x[3] - x[2]) / x[1] if x[3] and x[2] else None
                 for x in raw_data}
    return processed


def numeric_regular_hash():
    '''Code being benchmarked'''
    processed = {x: x * x for x in range(1001)}
    return processed


class TestCorrectness(TestCase):
    def test_regular_hash(self):
        self.maxDiff = None
        self.assertDictEqual({key: round(value, 7) if value else None for key, value in regular_hash().items()}, processed_data, 'Regular Hash is correct')

    def test_numeric_regular_hash(self):
        self.maxDiff = None
        self.assertDictEqual(numeric_regular_hash(), numeric_processed_data, 'Numeric Regular Hash is correct')


def main():
    '''Entry point'''

    with open(argv[1], newline='') as raw_data_csv:
        for row in reader(raw_data_csv):
            for i in range(1, 4):
                if row[i]:
                    row[i] = float(row[i])
            raw_data.append(row)

    with open(argv[2], newline='') as processed_data_csv:
        for row in reader(processed_data_csv):
            row[1] = None if row[1] == 'N/A' else float(row[1])
            processed_data[row[0]] = row[1]

    with open(argv[3], newline='') as numeric_processed_data_csv:
        for row in reader(numeric_processed_data_csv):
            numeric_processed_data[int(row[0])] = int(row[1])

    timed_iteration = int(argv[4])

    # Total, wallclock time for lots of runs.
    print(
        "Regular Hash:\t\t", timeit(regular_hash, number=timed_iteration), "\n",
        "Numeric Regular Hash:\t", timeit(numeric_regular_hash, number=timed_iteration), "\n",
        sep=''
    )

    # Verify correctness, and compare with other benchmarked code.
    suite = TestSuite()
    suite.addTest(TestCorrectness('test_regular_hash'))
    suite.addTest(TestCorrectness('test_numeric_regular_hash'))
    TextTestRunner().run(suite)


if __name__ == '__main__':
    main()

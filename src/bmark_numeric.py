#!/usr/bin/env python
'''Benchmark Runner'''

from timeit import timeit


def benchmark():
    '''Code being benchmarked'''
    processed = {x: x * x for x in range(1001)}
    return processed


# Total, wallclock time for lots of runs.
print(timeit(benchmark, number=10000))

# Verify correctness, and compare with other benchmarked code.
ret = benchmark()
for k, v in sorted(ret.items()):
    print(str(k) + ',' + str(v))

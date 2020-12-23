import sys
import os

def count_combinations(mem, n, adapters):
    if n not in mem:
        mem[n] = sum([count_combinations(mem, i, adapters) for i in range(n + 1, n + 4) if i in adapters])
    return mem[n]

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Number of combinations in which the adapters can be used from 0 to the largest adapter (adapter can be chained with another 1, 2 or 3 numbers lower)')
    numbers = [0] + [int(line) for line in f.readlines()]
    print('Result: {0}'.format(count_combinations({max(numbers) : 1}, 0, numbers)))
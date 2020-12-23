import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print("Find 2 numbers (a, b) that sum 2020, get its product, a * b")
    seen = {}
    target = 2020
    for line in f.readlines():
        n = int(line)
        if target - n in seen:
            print('{0} * {1} = {2}'.format(n, target - n, n * (target - n)))
        seen[n] = 1
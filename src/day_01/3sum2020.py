import sys
import os

def two_sum(target, numbers):
    seen = {}
    for n in numbers:
        if target - n in seen:
            return (target - n, n)
        seen[n] = 1
    return None

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print("Find 3 numbers (a, b, c) that sum 2020, get its product, a * b * c")
    target = 2020
    numbers = []
    for line in f.readlines():
        numbers.append(int(line))
    for i, n in enumerate(numbers):
        if i + 1 > len(numbers) - 2: # Avoid invalid index
            break
        result = two_sum(target - n, numbers[i + 1:])
        if result is not None:
            print('{0} * {1} * {2} = {3}'.format(n, result[0], result[1], n * result[0] * result[1]))
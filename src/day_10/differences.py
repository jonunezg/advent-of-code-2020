import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Number of 1 jolt diffrences times number of 3 jolt differences')
    numbers = [int(line) for line in f.readlines()]
    numbers = [0] + numbers + [max(numbers) + 3]
    numbers.sort()
    differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    print('Result: {0}'.format(differences.count(1) * differences.count(3)))
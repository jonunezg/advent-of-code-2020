import sys
import os

def two_sum(target, numbers):
    seen = {}
    for n in numbers.keys():
        if target - n in seen and n != target - n:
            return True
        seen[n] = 1
    return False


with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Find the first number which is not the sum of two of the previous 25 numbers')
    numbers = [int(line) for line in f.readlines()]
    preamble = {}
    window = 25
    for elem in numbers[:window]:
        preamble[elem] = preamble.get(elem, 0) + 1
    for i, elem in enumerate(numbers[window:]):
        if not two_sum(elem, preamble):
            print('Number: {0}'.format(elem))
            break
        preamble[numbers[i]] -= 1
        if preamble[numbers[i]] == 0:
            preamble.pop(numbers[i])
        preamble[elem] = preamble.get(elem, 0) + 1
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
    print('Add the min and max numbers of a continous range in the list that adds to the first invalid number')
    numbers = [int(line) for line in f.readlines()]
    preamble = {}
    window = 25
    invalid = 0
    for elem in numbers[:window]:
        preamble[elem] = preamble.get(elem, 0) + 1
    for i, elem in enumerate(numbers[window:]):
        if not two_sum(elem, preamble):
            print('Number: {0}'.format(elem))
            invalid = elem
            break
        preamble[numbers[i]] -= 1
        if preamble[numbers[i]] == 0:
            preamble.pop(numbers[i])
        preamble[elem] = preamble.get(elem, 0) + 1

    i = j = current = 0
    while True:
        if current < invalid:
            current += numbers[j]
            j += 1
        elif current > invalid:
            current -= numbers[i]
            i += 1
        else:
            break
    print('Sum: {0}'.format(min(numbers[i:j]) + max(numbers[i:j])))
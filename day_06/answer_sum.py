import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Count the number of unique responses on each group')
    groups = []
    answers = {}
    for line in [a.strip('\n') for a in f.readlines()]:
        if len(line) == 0:
            groups.append(answers)
            answers = {}
        else:
            for c in line:
                answers[c] = True
    print('Sum of group sizes: {0}'.format(sum([len(entry) for entry in groups])))
    
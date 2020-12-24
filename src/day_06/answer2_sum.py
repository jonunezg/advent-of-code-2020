import sys
import os

def common_responses(group):
    return sum([1 for answer_count in group.values() if answer_count == group['members']]) - 1

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Count the number of common responses on each group')
    groups = []
    answers = {}
    for line in [a.strip('\n') for a in f.readlines()]:
        if len(line) == 0:
            groups.append(answers)
            answers = {}
        else:
            answers['members'] = answers.get('members', 0) + 1
            for c in line:
                answers[c] = answers.get(c, 0) + 1
    print('Sum of group sizes: {0}'.format(sum([common_responses(entry) for entry in groups])))
    
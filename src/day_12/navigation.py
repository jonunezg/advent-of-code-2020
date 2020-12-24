import sys
import os


with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Get the Manhattan distance traveled')
    pos = (0, 0)
    heading = 90
    for k, value in [(line[0], int(line.strip('\n')[1:])) for line in f.readlines()]:
        if k in ('L', 'R'):
            heading += value * (1 if k == 'R' else -1)
            heading += 360 * (abs(heading) // 360 + 1)
            heading %= 360
        if k == 'F':
            pos = (pos[0] + value * (1 if heading == 90 else (-1 if heading == 270 else 0)), pos[1] + value * (1 if heading == 0 else (-1 if heading == 180 else 0)))
        if k in ('N', 'S', 'W', 'E'):
            pos = (pos[0] + value * (1 if k == 'E' else (-1 if k == 'W' else 0)), pos[1] + value * (1 if k == 'N' else (-1 if k == 'S' else 0)))
        print(k, value, pos, heading)
    print('Result: {0}'.format(sum([abs(a) for a in pos])))
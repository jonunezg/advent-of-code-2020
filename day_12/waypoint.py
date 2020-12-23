import sys
import os


with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Get the Manhattan distance traveled')
    pos = (0, 0)
    waypoint = (10, 1)
    for k, value in [(line[0], int(line.strip('\n')[1:])) for line in f.readlines()]:
        if k in ('L', 'R'):
            rotation = value % 360
            if k == 'L':
                rotation = 360 - rotation
            for _ in range(rotation // 90):
                waypoint = (waypoint[1], -waypoint[0])
        if k == 'F':
            pos = (pos[0] + value * waypoint[0], pos[1] + value * waypoint[1])
        if k in ('N', 'S', 'W', 'E'):
            waypoint = (waypoint[0] + value * (1 if k == 'E' else (-1 if k == 'W' else 0)), waypoint[1] + value * (1 if k == 'N' else (-1 if k == 'S' else 0)))
        print(k, value, pos, waypoint)
    print('Result: {0}'.format(sum([abs(a) for a in pos])))
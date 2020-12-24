import sys
import os

def get_dec(pattern, encoded_1):
    n = 0
    for c in pattern:
        n = (n << 1) | (1 if c == encoded_1 else 0)
    return n

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Get boarding pass Id, row * 8 + column, which are encoded using binary')
    lines = f.readlines()
    max_id = 0
    for line in lines:
        line = line.strip('\n')
        row = get_dec(line[:7], 'B')
        col = get_dec(line[7:], 'R')
        max_id = max(max_id, row * 8 + col)
    print('Max id: {0}'.format(max_id))
    
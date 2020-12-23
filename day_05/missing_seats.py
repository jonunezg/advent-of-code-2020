import sys
import os

def get_dec(pattern, encoded_1):
    n = 0
    for c in pattern:
        n = (n << 1) | (1 if c == encoded_1 else 0)
    return n

def get_id(line):
    return get_dec(line[:7], 'B') * 8 + get_dec(line[7:], 'R')

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Get the only available seat, must be between two used seats')
    occupied = [False] * 128 * 8
    for seat in [get_id(a.strip('\n')) for a in f.readlines()]:
        occupied[seat] = True
    for i in range(1, len(occupied) - 1):
        if occupied[i - 1] and occupied[i + 1] and not occupied[i]:
            print('Seat: {0}, row: {1}, col: {2}'.format(i, i // 8, i % 8))
    
import sys
import os

def gen_neighbours(coords):
    x, y, z, w = coords
    for i in range(81):
        if i != 40:
            yield (x + i // 27 % 3 - 1, y + i // 9 % 3 - 1, z + i // 3 % 3 - 1, w + i % 3 - 1)

def count_active_neighbours(coords, active):
    return sum([1 for neighbour in gen_neighbours(coords) if neighbour in active])

print('Do 6 iterations of game of life, Activate if 3 neighbours are active, do not deactivate if 2 or 3 neighbours are active')

active = {}
with open(os.path.dirname(__file__) + '/input.txt') as f:
    for y, line in enumerate([line.strip('\n') for line in f.readlines()]):
        for x, c in enumerate(line):
            if c == '#':
                active[(x, y, 0, 0)] = True
for _ in range(6):
    next_gen = {}
    for cube in active:
        if count_active_neighbours(cube, active) in(2, 3):
            next_gen[cube] = True
        processed = {}
        for neighbour in gen_neighbours(cube):
            if neighbour not in processed and neighbour not in active:
                if count_active_neighbours(neighbour, active) == 3:
                    next_gen[neighbour] = True
                processed[neighbour] = True
    active = next_gen
    print(len(active))
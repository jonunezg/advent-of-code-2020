import sys
import os

def is_valid_pos(layout, pos):
    x, y = pos
    return x >= 0 and x < len(layout) and y >= 0 and y < len(layout[0])

def occupied_neighbours(layout, seat):
    x, y = seat
    neighbours = [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x - 1, y), (x - 1, y - 1)]
    return sum([1 for n, k in neighbours if is_valid_pos(layout, (n, k)) and layout[n][k] == '#'])

def update_chairs(layout):
    updated = False
    occupied = 0
    update_map = [[False for _ in range(len(layout[0]))] for _ in range(len(layout))]
    for x in range(len(layout)):
        for y in range(len(layout[0])):
            update_map[x][y] = True if (layout[x][y] == 'L' and occupied_neighbours(layout, (x, y)) == 0) or (layout[x][y] == '#' and occupied_neighbours(layout, (x, y)) >= 4) else False
    for x in range(len(layout)):
        for y in range(len(layout[0])):
            if update_map[x][y]:
                layout[x][y] = 'L' if layout[x][y] == '#' else '#'
                updated = True
            occupied += 1 if layout[x][y] == '#' else 0
    return (updated, occupied)
     

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Simulate chair usage until stable and print number of used seats')
    layout = [list(line.strip('\n')) for line in f.readlines()]
    updated = True
    occupied = 0
    while updated:
        updated, occupied = update_chairs(layout)
        print(updated, occupied)
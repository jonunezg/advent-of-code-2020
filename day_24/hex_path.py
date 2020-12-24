from os import path

def generate_neighbors(coord):
    for neighbor in [[-1, 0], [1, 0], [-1, 1], [0, 1], [0, -1], [1, -1]]:
        yield tuple([a + b for a, b in zip(coord, neighbor)])

def count_black_neighbors(tiles, coord):
    return sum([1 for neighbor in generate_neighbors(coord) if tiles.get(neighbor, False)])

def next_black_tiles(tiles):
    processed, new_black = {}, {}
    for tile in tiles:
        if tiles[tile]:
            if count_black_neighbors(tiles, tile) in (1, 2):
                new_black[tile] = True
            for neighbor in generate_neighbors(tile):
                if neighbor not in processed and not tiles.get(neighbor, False) and count_black_neighbors(tiles, neighbor) == 2:
                    new_black[neighbor] = True
                processed[neighbor] = True
    return new_black

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Flip tiles by following directions')
    lines = [line.strip('\n') for line in f.readlines()]
    black_tiles = {}
    offsets = { 'w' : [-1, 0], 'e' : [1, 0], 'nw' : [-1, 1], 'ne' : [0, 1], 'sw' : [0, -1], 'se' : [1, -1] }
    for line in lines:
        coord = [0, 0]
        while line:
            if line[0] in ('e', 'w'):
                coord = [a + b for a, b in zip(coord, offsets[line[0]])]
                line = line[1:]
            else:
                coord = [a + b for a, b in zip(coord, offsets[line[0:2]])]
                line = line[2:]
        black_tiles[tuple(coord)] = not black_tiles.get(tuple(coord), False)
    print(sum([1 for tile in black_tiles if black_tiles[tile] == True]))

    print('Now do 100 generations of game of life and print the number of black tiles afterwards')
    for i in range(100):
        black_tiles = next_black_tiles(black_tiles)
    print(sum([1 for tile in black_tiles if black_tiles[tile] == True]))


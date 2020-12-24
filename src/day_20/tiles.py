from os import path

def get_edges(data):
    left = right = ''
    for row in data:
        left += row[0]
        right += row[-1]
    return [data[0], data[-1], left, right]

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Assemble image by rotating tiles, get the result of multiplying the ID of the corners')
    tiles = [tile for tile in f.read().split('\n\n') if tile != '']
    edges = {}
    matches = {}
    for tile in tiles:
        id, data = tile.split('\n')[0].split(' ')[1].strip(':'), tile.split('\n')[1:]
        for edge in get_edges(data):
            if edge in edges:
                matches[edges[edge]] = matches.get(edges[edge], 0) + 1
                matches[id] = matches.get(id, 0) + 1
            else:
                edges[edge] = id
                edges[edge[::-1]] = id
    res = 1
    for corner in [tile for tile in matches if matches[tile] == 2]:
        res *= int(corner)
    print(res)
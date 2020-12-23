from os import path

def get_edges(data):
    left = right = ''
    for row in data:
        left += row[0]
        right += row[-1]
    return [data[0], data[-1], left, right]

def print_pic(data):
    for row in data:
        print(row)
    print('')

def rotate(data):
    new_rows = [''] * len(data)
    for row in data[::-1]:
        for i, c in enumerate(row):
            new_rows[i] += c
    return new_rows

def flip(data):
    return [row[::-1] for row in data]

def get_neighbour(tiles, tile, matches, my_edge, edge_to_match):
    f = lambda data : data if get_edges(tiles[tile])[my_edge] == get_edges(data)[edge_to_match] else None
    for match in matches[tile]:
        new_data = apply_function_to_rotated_data(tiles[match], f)
        if new_data is not None:
            tiles[match] = new_data
            return match
    return None

def get_ids_in_row(tiles, tile, matches):
    row = [tile]
    while True:
        actual = len(row)
        new_element = get_neighbour(tiles, row[-1], matches, 3, 2)
        if new_element:
            row.append(new_element)
        if actual == len(row):
            return row

def orient_corner(tiles, corner, matches):
    for __ in range(2):
        for _ in range(4):
            if get_neighbour(tiles, corner, matches, 3, 2) is not None and get_neighbour(tiles, corner, matches, 1, 0) is not None:
                return
            tiles[corner] = rotate(tiles[corner])
        tiles[corner] = flip(tiles[corner])

def clear_edges(tiles):
    for tile, data in tiles.items():
        tiles[tile] = [row[1:-1] for row in data][1:-1]

def make_image(tiles, corner, matches):
    orient_corner(tiles, corner, matches)
    left = corner
    image = []
    ids = []
    while left is not None:
        ids.append(get_ids_in_row(tiles, left, matches))
        left = get_neighbour(tiles, left, matches, 1, 0)
    clear_edges(tiles)
    print(ids)
    for row in ids:
        image += stitch_pics(tiles, row)
    return(image)
        

def stitch_pics(tiles, row):
    data = []
    for i in range(len(tiles[row[0]])):
        r = ''
        for tile in [tiles[c] for c in row]:
            r += tile[i]
        data.append(r)
    return data


def clean_sea_monsters(data):
    for i, string in enumerate(data):
        data[i] = string.replace('O', '#')

sea_monster = [ '                  # ', \
                '#    ##    ##    ###', \
                ' #  #  #  #  #  #   ']

def paint_sea_monster(data, i, j, r, c):
    points = [(r + n // 20, c + n % 20) for n in range(60) if sea_monster[n // 20][n % 20] == '#' and data[r + n // 20][c + n % 20] == '#']
    if len(points) != 15:
        return
    for i, j in points:
        data[i] = data[i][:j] + 'O' + data[i][j + 1:]

def apply_function_to_rotated_data(data, f):
    for __ in range(2):
        for _ in range(4):
            result = f(data)
            if result is not None:
                return result
            data = rotate(data)
        data = flip(data)

def look_for_monsters(image):
    for r in range(len(image) - 2):
        for c in range(len(image[0]) - 19):
            paint_sea_monster(image, 0, 0, r, c)
    #print_pic(image)
    print(sum([row.count('#') for row in image]))
    clean_sea_monsters(image)

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Assemble image by rotating tiles and removing edges, identify the monster pattern and count the number of # left without monsters in the image')
    tiles_text = [tile for tile in f.read().split('\n\n') if tile != '']
    edges = {}
    matches = {}
    tiles = {}
    for tile in tiles_text:
        id, data = tile.split('\n')[0].split(' ')[1].strip(':'), tile.split('\n')[1:]
        tiles[id] = data
        for edge in get_edges(data):
            if edge in edges:
                matches[edges[edge]] = matches.get(edges[edge], []) + [id]
                matches[id] = matches.get(id, []) + [edges[edge]]
            else:
                edges[edge] = id
                edges[edge[::-1]] = id
    corners = [tile for tile in matches if len(matches[tile]) == 2]
    image = make_image(tiles, corners[0], matches)
    apply_function_to_rotated_data(image, look_for_monsters)

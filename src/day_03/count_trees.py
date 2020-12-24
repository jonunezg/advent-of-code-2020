import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print("Count the number of trees #, while going 1 down 3 right")
    trees = 0
    column = 0
    for line in f.readlines():
        line = line.strip('\n')
        trees += 1 if line[column] == '#' else 0
        print(line, column, trees)
        column = (column + 3) % len(line)
    print('Number of trees: {0}'.format(trees))
import sys
import os

def count_trees(lines, right, down):
    trees = 0
    column = 0
    row = 0
    while row < len(lines):
        line = lines[row].strip('\n')
        trees += 1 if line[column] == '#' else 0
        column = (column + right) % len(line)
        row += down
    print('Number of trees: {0}'.format(trees))
    return trees

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Count the number of trees #, while going 1,1 3,1 5,1 7,1 and 1,2 right and down and multiply')
    lines = f.readlines()
    print('Total: {0}'.format(count_trees(lines, 1, 1) * count_trees(lines, 3, 1) * count_trees(lines, 5, 1) * count_trees(lines, 7, 1) * count_trees(lines, 1, 2)))
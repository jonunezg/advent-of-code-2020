import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Print the 2020th and 30000000th numbers spoken, next number is 0 if the last number has never been spoken or the difference in turns from when it was last spoken')
    initial, seen, turn = [int(e) for e in f.readline().split(',')], {}, 1
    for n in initial[:len(initial) - 1]:
        seen[n], turn = turn, turn + 1
    cur = initial[-1]
    while turn < 30000000:
        seen[cur], turn, cur = turn, turn + 1, 0 if cur not in seen else turn - seen[cur]
        if turn in (2020, 30000000):
            print('Turn: {0}, number: {1}'.format(turn, cur))
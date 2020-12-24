import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print("Validate passwords and print the number of valid passwords")
    valid = 0
    for line in f.readlines():
        r, l, p = line.replace(':', '').split()     # 1-3 f: eafeaw
        r = [int(a) for a in r.split('-')]          #  r  l     p
        c = p.count(l)
        # 'l' must appear at least 'r[0]' and at most 'r[1]' times in 'p'
        if (c >= r[0] and c <= r[1]):
            valid += 1
        print(r, l, p, valid)
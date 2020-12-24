import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print("Validate passwords and print the number of valid passwords")
    valid = 0
    for line in f.readlines():
        r, l, p = line.replace(':', '').split()     # 1-3 f: eafeaw
        r = [int(a) for a in r.split('-')]          #  r  l     p
        # Exactly one of the positions (1 indexed) in 'p' marked by 'r' should be equal to 'l'
        if sum([1 for pos in r if pos - 1 < len(p) and p[pos - 1] == l]) == 1:
            valid += 1
        print(r, l, p, valid)
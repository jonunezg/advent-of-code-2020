from os import path

def update(n, subject):
    return (n * subject) % 20201227

def apply(subject, i):
    n = 1
    for _ in range(i):
        n = update(n, subject)
    return n

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Get the encryption_key')
    public_keys = [int(line.strip('\n')) for line in f.readlines()]
    n, i = 1, 0
    while n != public_keys[0]:
        n = update(n, 7)
        i += 1
    print(apply(public_keys[1], i))
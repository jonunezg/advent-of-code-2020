from os import path

def update(n, subject):
    return (n * subject) % 20201227

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Get the encryption_key')
    n, encryption_key, public_keys = 1, 1, [int(line.strip('\n')) for line in f.readlines()]
    while n != public_keys[0]:
        n, encryption_key = update(n, 7), update(encryption_key, public_keys[1])
    print(encryption_key)
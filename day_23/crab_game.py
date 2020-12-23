from os import path

def play(sequence):
    current, next_3, rest = sequence[0], sequence[1:4], sequence[4:]
    for i in range(1, 9):
        cup = int(current) - i
        cup += 9 if cup < 1 else 0
        cup = rest.find(str(cup))
        if cup != -1:
            return rest[:cup + 1] + next_3 + (rest[cup + 1:] if cup + 1 < len(rest) else '') + current

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Play the game and print the sequence')
    sequence = f.read().strip('\n')
    for i in range(100):
        sequence = play(sequence)
    i = sequence.find('1')
    print((sequence[i + 1:] if i + i < len(sequence) else '') + sequence[:i])
    
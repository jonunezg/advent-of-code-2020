from os import path

def next(candidate, exclusions, max_value):
    while candidate in exclusions:
        candidate = candidate - 1 if candidate > 1 else max_value
    return candidate

def play(s, cur):
    next_3 = [s[cur], s[s[cur]], s[s[s[cur]]]] # Get 3 elements to move
    s[cur] = s[next_3[2]] # Move them out of the list
    i = next(cur, next_3 + [cur], len(s) - 1) # Find the destination
    s[i], s[next_3[2]] = next_3[0], s[i] # Move 3 elements to destination
    return s[cur] # Return right neighbor of current value

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Play the game and print the product of the two numbers to the right of 1')
    sequence = [max(10, i + 1) for i in range(1000001)]
    input = f.read().strip('\n')
    for i, c in enumerate(input[:-1]):
        sequence[int(c)] = int(input[i + 1])
    sequence[-1] = int(input[0])
    current = int(input[0])
    for i in range(10000000):
        current = play(sequence, current)
    print(sequence[1] * sequence[sequence[1]])
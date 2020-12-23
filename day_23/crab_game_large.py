from os import path

def play(s, cur):
    next_3 = [s[cur], s[s[cur]], s[s[s[cur]]]]
    s[cur] = s[next_3[2]]
    i = cur - 1
    while True:
        if i == 0:
            i = len(s) - 1
        if i not in next_3:
            break
        i -= 1
    s[i], s[next_3[2]] = next_3[0], s[i]
    return s[cur]

with open(path.dirname(__file__) + '/input2.txt') as f:
    print('Play the game and print the product of the two numbers to the right of 1')
    sequence = [i + 1 for i in range(1000001)]
    input = f.read().strip('\n')
    for i, c in enumerate(input[:-1]):
        sequence[int(c)] = int(input[i + 1])
    sequence[int(input[-1])] = 10
    sequence[-1] = int(input[0])
    current = int(input[0])
    for i in range(10000000):
        current = play(sequence, current)
    print(sequence[1], sequence[sequence[1]])
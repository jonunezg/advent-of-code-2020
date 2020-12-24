from os import path

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Play the game and print the winning score')
    d1, d2 = [[int(a) for a in cards.strip().split('\n')[1:]] for cards in f.read().split('\n\n')]
    while len(d1) and len(d2):
        top1, top2 = d1[0], d2[0]
        d1, d2 = d1[1:], d2[1:]
        if top1 >= top2:
            d1.append(top1)
            d1.append(top2)
        else:
            d2.append(top2)
            d2.append(top1)
    winner = d1 if d1 else d2
    print(sum([(i + 1) * x for i, x, in enumerate(winner[::-1])]))

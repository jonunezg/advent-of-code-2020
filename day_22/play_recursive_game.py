from os import path

def play(decks, mem, depth):
    original = tuple([deck[:] for deck in decks])
    if original not in mem:
        previous = {}
        while not [True for deck in decks if len(deck) == 0]:
            if decks in mem:
                return mem[decks]
            if decks in previous:
                return (0, decks)
            previous[decks] = True
            cards = [deck[0] for deck in decks]
            decks = [deck[1:] for deck in decks]
            i = play(tuple([deck[:cards[i]] for i, deck in enumerate(decks)]), mem, depth + 1)[0] if len([True for i, deck in enumerate(decks) if cards[i] <= len(deck)]) == len(decks) else cards.index(max(cards))
            decks[i] = decks[i] + (cards[i], cards[i - 1])
            decks = tuple(decks)
        for p in previous:
            mem[p] = (0 if len(decks[0]) else 1, decks)
    return mem[original]

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Play the game with the recursive set of rules and print the winning score')
    decks = tuple([tuple([int(a) for a in cards.strip().split('\n')[1:]]) for cards in f.read().split('\n\n')])
    winner, result = play(decks, {}, 0)
    print(sum([(i + 1) * card for i, card in enumerate(result[winner][::-1])]))
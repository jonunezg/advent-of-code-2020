import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('How many colors can hold a gold bag')
    rules = {}
    for parent, children in [(rule.split(' bags')[0], rule.strip(' .\n').split('contain ')[1].split(', ')) for rule in f.readlines()]:
        for child in children:
            if child == "no other bags":
                break
            words = child.split(' ')
            color = ' '.join((words[1:3]))
            rules[color] = rules.get(color, [])
            rules[color].append(parent)
    seen = ['shiny gold']
    colors = ['shiny gold']
    while colors:
        color = colors.pop()
        new_colors = [parent for parent in rules.get(color, []) if parent not in seen]
        colors.extend(new_colors)
        seen.extend(new_colors)
    print("Shiny gold bags can be held by {0} other color bags".format(len(seen) - 1))
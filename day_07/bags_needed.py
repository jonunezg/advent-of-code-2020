import sys
import os

def bags_needed(rules, color):
    return 1 + sum([n * bags_needed(rules, child) for n, child in rules.get(color, [])])

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('How many bags are needed in total')
    rules = {}
    for parent, children in [(rule.split(' bags')[0], rule.strip(' .\n').split('contain ')[1].split(', ')) for rule in f.readlines()]:
        rules[parent] = [(int(child.split(' ')[0]), ' '.join((child.split(' ')[1:3]))) for child in children if child != "no other bags"]
    print('Need {0} bags'.format(bags_needed(rules, 'shiny gold') - 1))
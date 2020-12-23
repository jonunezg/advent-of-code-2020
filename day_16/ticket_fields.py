import sys
import os

categories_zone = 0
ticket_zone = 1
nearby_zone = 2

def in_range(n, r):
    return n >= r[0] and n <= r[1]

def is_n_invalid(n, ranges):
    return True if len([True for r in ranges if in_range(n, r)]) == 0 else False

def is_ticket_valid(ticket, ranges):
    return len([True for n in ticket if is_n_invalid(n, ranges)]) == 0

lines = []
with open(os.path.dirname(__file__) + '/input.txt') as f:
    lines = f.readlines()

print('Fit each category to its column according to the valid ranges, and')
print('multiply the value of all categories that start with "departure" in your ticket')
zone = categories_zone
categories = {}
all_ranges = []
tickets = []
valid_counts = {}
my_ticket = []
for line in lines:
    line = line.strip('\n')
    if line == '':
        continue
    if line in ('your ticket:', 'nearby tickets:'):
        zone += 1
        continue

    if zone == categories_zone:
        category, ranges = line.split(': ')
        ranges = [[int(a) for a in pair.split('-')] for pair in ranges.split(' or ')]
        categories[category] = ranges
        all_ranges += ranges
    else:
        ticket = [int(v) for v in line.split(',')]
        if zone == ticket_zone:
            my_ticket = ticket
        elif zone == nearby_zone:
            if is_ticket_valid(ticket, all_ranges):
                tickets.append(ticket)
for ticket in tickets:
    for col, n in enumerate(ticket):
        for k in categories:
            if not is_n_invalid(n, categories[k]):
                # For each ticket, count if current column is valid on each category
                valid_counts[(k, col)] = valid_counts.get((k, col), 0) + 1
found = {}
while len(found) < len(my_ticket):
    # Find one category which can only fit in only one column
    for category in categories:
        counts = [valid_counts.get((category, col), 0) for col in range(len(my_ticket))]
        if counts.count(len(tickets)) == 1:
            # Choose this category
            index = counts.index(len(tickets))
            found[category] = index
            for k in categories:
                # Discard all categories that might fit in this column
                valid_counts[(k, index)] = valid_counts.get((k, index), 0) - 1
            break
result = 1
for k, value in found.items(): 
    if k.startswith('departure'):
        result *= my_ticket[value]
print(result)

import sys
import os

fields_zone = 0
ticket_zone = 1
nearby_zone = 2

def in_range(n, r):
    #print(n,r,n >= r[0] and n <= r[1])
    return n >= r[0] and n <= r[1]

def is_invalid(n, ranges):
    return True if len([True for r in ranges if in_range(n, r)]) == 0 else False

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('From nearby tickets, add those values which do not match any of the valid ranges')
    lines = f.readlines()
    zone = fields_zone
    fields = {}
    all_ranges = []
    invalid = []
    for line in lines:
        line = line.strip('\n')
        if line == '':
            continue
        if line == 'your ticket:':
            zone = ticket_zone
            continue
        elif line == 'nearby tickets:':
            zone = nearby_zone
            continue
        if zone == fields_zone:
            category, ranges = line.split(': ')
            ranges = [[int(a) for a in pair.split('-')] for pair in ranges.split(' or ')]
            fields[category] = ranges
            all_ranges += ranges
        elif zone == ticket_zone:
            continue
        elif zone == nearby_zone:
            invalid += [int(v) for v in line.split(',') if is_invalid(int(v), all_ranges)]
            
    print(sum(invalid), invalid)
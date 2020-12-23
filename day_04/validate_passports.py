import sys
import os


with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Validate passports have 7 mandatory fields')
    lines = f.readlines()
    current = {}
    documents = []
    for line in lines:
        line = line.strip('\n')
        if len(line) == 0:
            documents.append(current)
            current = {}
        else:
            for key, value in [entry.split(':') for entry in line.split(' ')]:
                current[key] = value
    expected = {'byr':0, 'iyr':0, 'eyr':0, 'hgt':0, 'hcl':0, 'ecl':0, 'pid':0}
    valid = 0
    for document in documents:
        present = 0
        for key in document:
            present += 1 if key in expected else 0
        valid += 1 if present == 7 else 0
    print('Valid: {0}'.format(valid))

import sys
import os
import string


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

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not

    expected = {'byr':0, 'iyr':0, 'eyr':0, 'hgt':0, 'hcl':0, 'ecl':0, 'pid':0}
    valid = 0
    for document in documents:
        present = 0
        for key, value in document.items():
            if  (key == 'byr' and len(value) == 4 and value.isnumeric() and int(value) >= 1920 and int(value) <= 2002) or \
                (key == 'iyr' and len(value) == 4 and value.isnumeric() and int(value) >= 2010 and int(value) <= 2020) or \
                (key == 'eyr' and len(value) == 4 and value.isnumeric() and int(value) >= 2020 and int(value) <= 2030) or \
                (key == 'hgt' and ((len(value) == 5 and value[:3].isnumeric() and int(value[:3]) >= 150 and int(value[:3]) <= 193 and value[3:] == "cm") or (len(value) == 4 and value[:2].isnumeric() and int(value[:2]) >= 59 and int(value[:2]) <= 76 and value[2:] == "in"))) or \
                (key == 'hcl' and len(value) == 7 and value[0] == '#' and all(c in string.hexdigits for c in value[1:])) or \
                (key == 'ecl' and value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')) or \
                (key == 'pid' and len(value) == 9 and value.isnumeric()):
                present += 1
        valid += 1 if present == 7 else 0
    print('Valid: {0}'.format(valid))
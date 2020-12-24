import sys
import os

def gen_combinations(base, rest, addresses):
    if rest == '':
        addresses.append(base)
    else:
        if rest[0] == 'X':
            gen_combinations(base + '0', rest[1:], addresses)
            gen_combinations(base + '1', rest[1:], addresses)
        else:
            gen_combinations(base + rest[0], rest[1:], addresses)

def address_to_int(address_string):
    address = 0
    for c in address_string:
        address = (address << 1) + (1 if c == '1' else 0)
    return address

def get_addresses(base, mask):
    onebit = 1 << 35
    res = ''
    for c in mask:
        res = res + (('1' if base & onebit != 0 else '0') if c == '0' else ('1' if c == '1' else 'X'))
        onebit >>= 1
    addresses = []
    gen_combinations('', res, addresses)
    for m in addresses:
        yield address_to_int(m)

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Sum values on memory left behind after applying asignment with masks')
    instructions = [line.replace('mask = ', '').replace('mem[', '').replace('] = ', ',').strip('\n').split(',') for line in f.readlines()]
    mask = ''
    mem = {}
    for ins in instructions:
        if len(ins) == 1:
            mask = ins[0]
        else:
            base_address, value = int(ins[0]), int(ins[1])
            for address in get_addresses(base_address, mask):
                mem[address] = value
    print('Sum: {0}'.format(sum([value for value in mem.values()])))
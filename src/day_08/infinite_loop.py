import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Print the value of acc just before executing any instruction for a second time')
    acc = pc = 0
    executed = {}
    program = [(line.split(' ')[0], int(line.split(' ')[1])) for line in f.readlines()]
    while True:
        if pc in executed:
            print('Acc: {0}'.format(acc))
            break
        executed[pc] = True
        mnemonic, value = program[pc]
        acc += value if mnemonic == 'acc' else 0
        pc += value if mnemonic == 'jmp' else 1

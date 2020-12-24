import sys
import os

def run_program(program):
    acc = pc = 0
    executed = {}
    while True:
        if pc in executed or pc == len(program):
            return (acc, True if pc in executed else False) # Loop or EOF
        executed[pc] = True
        mnemonic, value = program[pc]
        acc += value if mnemonic == 'acc' else 0
        pc += value if mnemonic == 'jmp' else 1

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Change just 1 jmp to nop or nop to jmp until program reaches end and print Acc')
    program = [(line.split(' ')[0], int(line.split(' ')[1])) for line in f.readlines()]
    for i in range(len(program)):
        mnemonic, value = program[i]
        if mnemonic == 'jmp' or mnemonic == 'nop':
            old, program[i] = program[i], ('nop' if mnemonic == 'jmp' else 'jmp', value)
            acc, loop = run_program(program)
            if not loop:
                print('Acc: {0}'.format(acc))
                break
            program[i] = old # Restore program
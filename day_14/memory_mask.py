import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Sum values on memory left behind after applying asignment with masks')
    instructions = [line.replace('mask = ', '').replace('mem[', '').replace('] = ', ',').strip('\n').split(',') for line in f.readlines()]
    onemask, zeromask, mem = 0, 1, {}
    for ins in instructions:
        if len(ins) == 1:
            onemask, zeromask = 0, 1
            for c in ins[0]:
                onemask <<= 1
                zeromask <<= 1
                onemask |= 1 if c == '1' else 0
                zeromask |= 0 if c == '0' else 1
        else:
            address, value = int(ins[0]), int(ins[1])
            if (1 << 36) - 1 < (value | onemask) & zeromask:
                print('Error', (value | onemask) & zeromask, ins, value, onemask, zeromask)
                break
            mem[address] = (value | onemask) & zeromask
    print('Sum: {0}'.format(sum([v for v in mem.values()])))
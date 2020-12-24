import sys
import os

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Find the earliest T at which the first bus departs and each bus not X departs Y minutes after T according to their offset on the list')
    t, step = 0, 1
    for offset, freq in [(offset, int(freq)) for offset, freq in enumerate([e for e in f.readlines()[1].strip('\n').split(',')]) if freq != 'x']:
        while (t + offset) % freq != 0:
            t += step
        step *= freq # Step becomes least common multiple of matched frequencies, just multiply as they are all prime numbers
        print ('Matched freq: {0}, new step: {1}, at t: {2}'.format(freq, step, t))
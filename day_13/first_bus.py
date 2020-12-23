import sys
import os


with open(os.path.dirname(__file__) + '/input.txt') as f:
    print('Get the ID of the first bus you can take times the minutes that you will have to wait')
    lines = f.readlines()
    arrive_time = int(lines[0])
    current, id = 999999999, 0
    for bus in [int(bus) for bus in lines[1].strip('\n').split(',') if bus != 'x']:
        time_to_wait = bus - arrive_time % bus
        time_to_wait = 0 if time_to_wait == bus else time_to_wait
        if current > time_to_wait:
            current, id = time_to_wait, bus
    print("Bus {0}, wait {1} minutes, result: {2}".format(id, current, id * current))
#!/usr/bin/env python3

ts = 0

with open("charlie.memtrace") as f:
    while(1):
        access = f.readline()
        if not access:
            break

        access = access.strip('\n').split(' ')
        access = [int(x, 16) for x in access]

        if access[0] == 0x0: # Load
            print("{} {} {}".format(hex(access[2]), "READ", ts))
        elif access[0] == 0x1: # Store
            print("{} {} {}".format(hex(access[2]), "WRITE", ts))

        ts += 4

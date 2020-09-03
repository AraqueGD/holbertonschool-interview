#!/usr/bin/python3

""" Log parsing Task """

import sys


def printsts(dic, size):
    """ Displayinformation """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

file_size = 0
size = 0

try:
    for line in sys.stdin:
        if file_size != 0 and file_size % 10 == 0:
            printsts(sts, size)

        stlist = line.split()
        file_size += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in sts:
                sts[stlist[-2]] += 1
        except:
            pass
    printsts(sts, size)


except KeyboardInterrupt:
    printsts(sts, size)
    raise

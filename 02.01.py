#!/usr/bin/python3

import sys
import re

def calc_area(l, w, h):
    side1 = l * w
    side2 = w * h
    side3 = l * h
    print("side1: %d side2: %d side3: %d" % (side1, side2, side3))
    area = 2*side1 + 2*side2 + 2*side3
    print("basic area: %d" % area)
    if side1 < side2:
        if side1 < side3:
            print("Adding %d from side1" % side1)
            area += side1
        else:
            print("Adding %d from side3" % side3)
            area += side3
    else:
        if side2 < side3:
            print("Adding %d from side2" % side2)
            area += side2
        else:
            print("Adding %d from side3" % side3)
            area += side3
    return area

# Test 1:
#box = "2x3x4"
# Test 2:
#box = "1x1x10"

#print("box: %s" % box)
#d = re.split('x', box)
#area = calc_area(int(d[0]), int(d[1]), int(d[2]))
#print("area: %d" % area)

total_area = 0
filepath = 'input.txt'
with open(filepath) as fp:
    box = fp.readline().rstrip()
    while box:
        print("box: %s" % box)
        d = re.split('x', box)
        area = calc_area(int(d[0]), int(d[1]), int(d[2]))
        print("area: %d" % area)
        total_area += area
        print("total area: %d" % total_area)
        box = fp.readline().rstrip()

print("Total area: %d" % total_area)

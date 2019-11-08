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

def calc_length(l, w, h):
    p1 = 2 * l + 2 * w 
    p2 = 2 * w + 2 * h
    p3 = 2 * l + 2 * h
    length = 0
    if p1 < p2:
        if p1 < p3:
            length = p1
        else:
            length = p3
    else:
        if p2 < p3:
            length = p2
        else:
            length = p3
    length += l * w * h
    return length

# Test 1:
#box = "2x3x4"
# Test 2:
#box = "1x1x10"

#print("box: %s" % box)
#d = re.split('x', box)
#length = calc_length(int(d[0]), int(d[1]), int(d[2]))
#print("length: %d" % length)

total_length = 0
filepath = 'input.txt'
with open(filepath) as fp:
    box = fp.readline().rstrip()
    while box:
        print("box: %s" % box)
        d = re.split('x', box)
        length = calc_length(int(d[0]), int(d[1]), int(d[2]))
        print("length: %d" % length)
        total_length += length
        print("total length: %d" % total_length)
        box = fp.readline().rstrip()

print("Total length: %d" % total_length)

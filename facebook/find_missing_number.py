#!/bin/env python
from collections import defaultdict

# example input 5
# 1 11 31 41 51
# output 21

N = int(raw_input())
l=raw_input()
list=[int(elem) for elem in l.split()]

dict={}
dict = defaultdict(int)
for i in xrange(N-1):
    res = list[i+1] - list[i]
    dict[res] += 1

difference=min(dict, key=dict.get)

for i in xrange(N-1):
    res = list[i+1] - list[i]
    if res == difference:
       print list[i-1] + difference
       break


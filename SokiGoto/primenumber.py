#!/bin/env python3
import sys

num = int(sys.argv[1])

li = []

while num != 1:
    for i in range(2, num+1):
        if num % i == 0:
            num = num // i
            li.append(i)

li.sort()

print(li, end="")

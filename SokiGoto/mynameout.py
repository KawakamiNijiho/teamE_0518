#!/usr/bin
import sys

args = sys.argv

if len(args) < 2:
    print("Please enter name on arg.")
    exit(1)
    
name = args[1]

print("Hello {:} !".format(name), end="")

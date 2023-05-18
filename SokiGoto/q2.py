#!/usr/bin
import sys

args = sys.argv

# 引数をint1, int2, int3にint型にして代入
int1 = int(args[1])
int2 = int(args[2])
int3 = int(args[3])

# int1, int2, int3を足してprintで出力
print(int1 + int2 + int3, end="")

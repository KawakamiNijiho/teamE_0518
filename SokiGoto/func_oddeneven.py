#!/bin/env python3
import sys

args = list(map(int, sys.argv[1:]))


# 関数を定義
def calcvalue(num):
    # あまりを算出
    mod = num % 2

    # あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")


for i in range(len(args)):
    calcvalue(args[i])

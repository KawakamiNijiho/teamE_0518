#!/bin/env python3
import sys

num = int(sys.argv[1])

sum_num = 0

# numを足し続ける
while True:
    sum_num += num
    # 合計sum_numが100か判定
    if sum_num == 100:
        print("Just 100!", end="")
        exit(0)
    # 合計sum_numが100を超えているか判定
    elif sum_num > 100:
        print("Over!", end="")
        exit(0)

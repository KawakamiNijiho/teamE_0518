#!/bin/env python3
import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv

distances = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35
    }

# 距離を計算
try:
    distance = Decimal(str(abs(distances[args[2]] - distances[args[1]]))).quantize(Decimal("0.01"), ROUND_HALF_UP)
    # 距離を出力
    print(distance, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="", file=sys.stderr)
    exit(0)

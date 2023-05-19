import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

station1 = args[1]
station2 = args[2]

# 辞書型に新幹線駅名と東京駅からの距離を定義
stations = {
    "東京":0.00,
    "品川":6.78,
    "新横浜":25.54,
    "名古屋":342.02,
    "京都":476.31,
    "新大阪":515.35
}
# 第二引数と第三引数に設定した駅名間の距離を計算し出力（少数第二位まで）

try:
    distance = stations[station1] - stations[station2]
    distance = abs(distance)
    distance = Decimal(str(distance)).quantize(Decimal("0.01"),rounding = ROUND_HALF_UP)
    print(distance, end="")

except:
    print("のぞみの停車駅を引数に設定してください", end="")




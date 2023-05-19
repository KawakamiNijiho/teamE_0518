# 引数モジュール
import sys
args = sys.argv
# 変数を定義
num = int(args[1])
sum = 0

# 100以上になるまで足し続ける繰り返し
while sum < 100:
    sum = sum + num

# 100か100以上かを判断し、処理決定
if sum == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")



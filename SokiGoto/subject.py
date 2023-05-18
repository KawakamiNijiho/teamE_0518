import sys

args = sys.argv

# scoreに点数すべてをint型の配列に入れる
score = list(map(int, args[1:4]))

# 不合格か合格かの条件で分岐して出力を行う
if ((score[0] >= 70 and score[1] >= 70 and score[2] >= 70) or (sum(score) >= 220)) \
    and (score[0] >= 50 and score[1] >= 50 and score[2] >= 50):
    print("合格", end="")
else:
    print("不合格", end="")

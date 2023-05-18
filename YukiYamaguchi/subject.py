# 引数のモジュールをインポート
import sys
args = sys.argv
# 変数に引数を代入
math = int(args[1])
jap = int(args[2])
eng = int(args[3])
total = math+jap+eng

# 合否判定の条件一つ目
if (math >= 70 and jap >= 70 and eng >= 70) or total >=220:
    # 合否判定の条件二つ目
    if math >= 50 and jap >= 50 and eng >= 50:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")


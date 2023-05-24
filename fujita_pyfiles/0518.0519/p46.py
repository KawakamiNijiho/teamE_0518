#モジュールインポート
import sys 

#変数numに引数受取
args=sys.argv
num=int(args[1])

#合計用の変数sumを用意
sum =0

#ループ
while sum <100:
    sum += num
    if sum == 100:
        print("Just 100!",end="")
if sum > 100:
    print("Over!",end="")

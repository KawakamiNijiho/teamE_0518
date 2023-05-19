#モジュールインポート
import sys

#引数受取
args=sys.argv
sentence=args[1]
num=int(args[2])

#文字分割
sp_sent=sentence.split(" ")

#出力
print(sp_sent[num-1],end="")
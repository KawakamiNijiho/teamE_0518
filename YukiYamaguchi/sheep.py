# 引数モジュール
import sys
args = sys.argv
sheep = args[1]

# 引数分ひつじが何匹かをカウントする
for i in range(1, int(sheep)+1):
    print("ひつじが" +str(i)+ "匹")

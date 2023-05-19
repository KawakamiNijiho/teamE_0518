import sys
args = sys.argv
# 変数を定義
eng = args[1]
pos = int(args[2])

# 文章を分割
sentence = eng
split_sentence = sentence.split(" ")

# 指定した部分の単語を表示
print(split_sentence[pos-1],end="")
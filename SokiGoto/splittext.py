#!/bin/env python3
import sys

# tmpに第2引数を代入し、indexに第2引数をint型で代入する。
tmp = sys.argv[1]
index = int(sys.argv[2]) - 1

# tmpをsplitして配列にしwordsに代入する。
words = tmp.split()

# wordsのindex番目を出力する。
print(words[index], end="")

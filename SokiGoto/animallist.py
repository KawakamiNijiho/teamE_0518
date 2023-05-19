#!/bin/env python3
import sys

# 第2引数をindex,第3引数をanimalに代入する
index = int(sys.argv[1])
animal = sys.argv[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# animalsのindexにanimalを代入する
animals.insert(index, animal)

# animalsの一番最後を消す
animals.pop()

# animalsを昇順にソートする
animals.sort()

# anamalsを出力する
print(animals, end="")

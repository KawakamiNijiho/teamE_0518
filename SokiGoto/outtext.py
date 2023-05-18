#!/usr/bin
import sys

args = sys.argv

#引数が一つもなかったらエラー文を出力して終了
if len(args) < 2:
    print("Please enter name on arg.", file=sys.stderr)
    exit(1)
    
dont_like_food = args[1]

print("I don't like {}".format(dont_like_food), end="")

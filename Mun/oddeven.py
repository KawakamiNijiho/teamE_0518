import sys
agrs = sys.argv

number = int(agrs[1])

if number%2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")


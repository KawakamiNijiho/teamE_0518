import sys
args = sys.argv
num = int(args[1])

sum = 0

while sum < 100:
    sum = num + sum
else:
    if sum == 100:
        print("Just 100!",end="")
    else:
        print("Over!",end="")
        
      
import sys
args=sys.argv
sentence=args[1]
num=int(args[2])
sp_sent=sentence.split(" ")
print(sp_sent[num-1],end="")
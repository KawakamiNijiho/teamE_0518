import sys
args  = sys.argv
en_sentence = args[1]
num = int(args[2])

en_list = en_sentence.split(" ")
print(en_list[num-1], end="")
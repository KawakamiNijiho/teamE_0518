import sys
args  = sys.argv
math_score = int(args[1])
japanese_score = int(args[2])
english_score = int(args[3])

total_score = math_score + japanese_score + english_score

if(total_score >= 220 and (math_score >=50) and (japanese_score >= 50)and(english_score >= 50))or((math_score >= 70)and(japanese_score >= 70)and(english_score >= 70)):
        print("合格", end="")
else:
    print("不合格", end="")
import sys
args=sys.argv
math=int(args[1])
nl=int(args[2])
eng=int(args[3])
sum=math+nl+eng
bool_1=((math >= 70) and (nl >= 70) and (eng >=70))or(sum>=220)
bool_2=((math >= 50) and (nl >= 50) and (eng >= 50))
if bool_1 and bool_2:
    
    print("合格",end="")
else:
    print('不合格',end="")
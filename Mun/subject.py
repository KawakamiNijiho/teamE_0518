import sys
agrs = sys.argv

mat = int(agrs[1])
jpa = int(agrs[2])
eng = int(agrs[3])
total = mat + jpa + eng;

if (mat >= 70 and jpa >= 70 and eng >= 70) or (total >= 220) and (mat >= 50 and jpa >= 50 and eng >= 50):
    print("合格",end="")   
else:
    print("不合格",end="")



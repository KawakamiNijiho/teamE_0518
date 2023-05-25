import sys

mat,jpa,eng = sys.argv[1:]

m = int(mat)
j = int(jpa)
e = int(eng)

total = sum([m,j,e])


if (m >= 70 & j >= 70 & e >= 70) or (total >= 220) and \
    (m >= 50 & j >= 50 & e >= 50):        
    print("合格",end="")   
else:
    print("不合格",end="")



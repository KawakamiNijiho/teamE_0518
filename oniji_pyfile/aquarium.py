import sys
args = sys.argv
num = (args[1])
adult =int(args[2])
child =int(args[3])

# numを年、月、日に分割
y =int(num[0:4])
m =int(num[4:6])
d =int(num[6:8])

# 曜日を算出
from datetime import date
dt = date(y,m,d)
v = dt.strftime("%a")

# 料金の設定
if v == "Sat" or v == "Sun":
    sum = adult * 2400 + child * 1500
else:
    sum = adult * 2000  + child * 1200

print(sum)

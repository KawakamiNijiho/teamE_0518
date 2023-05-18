import sys
from decimal import Decimal, ROUND_HALF_UP

# 引数をsalaryにint型で代入
salary = int(sys.argv[1])

# salary が100万を超えるかで税額を変える
if salary > 1000000:
    tax = Decimal(str(1000000 * 0.1 + (salary - 1000000) * 0.2)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
else:
    tax = Decimal(str(salary * 0.1)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
# 支給額を計算
pay = salary - tax
# 結果を出力
print("支給額:{0}、税額:{1}".format(pay, tax), end="")
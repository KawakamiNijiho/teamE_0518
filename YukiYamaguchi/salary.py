# 引数モジュールをインポート
import sys
args = sys.argv
salary = int(args[1])
# 四捨五入モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

#条件分岐
#引数が100万を超える場合は、100万を超えた部分を20%で税額換算して変数に税額と支給額を代入
if salary > 1000000:
    tax = 100000+(salary-1000000)*0.2
#引数が100万以下の場合、税率10％換算
else:
    tax = salary*0.1

tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
paypay = salary-tax

print("支給額:"+str(paypay)+"、"+"税額:"+str(tax), end="")
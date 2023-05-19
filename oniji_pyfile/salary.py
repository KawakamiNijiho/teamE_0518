import sys
from decimal import Decimal, ROUND_HALF_UP
args  = sys.argv
salary = int(args[1])

if(salary <= 1000000):
   tax = salary * 0.1
else:
   tax = 1000000 * 0.1 + (salary-1000000) * 0.2

tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
pay = salary - tax


print(f'支給額:{pay} 、税額:{tax}',end="")
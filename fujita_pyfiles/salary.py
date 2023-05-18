import sys
args=sys.argv
money=int(args[1])
if money > 1000000:
    tax=100000+(money-1000000)*0.2
else:
    tax=money*0.1
payment=money-tax
print(f"支給額:{int(payment)}、税額:{int(tax)}",end="")
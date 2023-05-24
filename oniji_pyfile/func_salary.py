def calcsalary(salary):
    if(salary <= 1000000):
     tax = salary * 0.1
    else:
     tax = 1000000 * 0.1 + (salary-1000000) * 0.2

    from decimal import Decimal, ROUND_HALF_UP
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    pay = int(salary - tax)

    

    print(f"給与：{salary}、支給額：{pay}、税額{tax}")

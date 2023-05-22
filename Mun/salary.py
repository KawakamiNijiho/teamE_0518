import sys

def calculate_tax_and_net_salary(gross_salary):
    # 税率の設定
    tax_rate_over_million = 0.2  # 給与額の100万円を超える部分は20%
    tax_rate_under_million = 0.1  # 給与額の100万円以下の部分は10%

    if gross_salary > 1_000_000:
        over_million = gross_salary - 1_000_000
        under_million = 1_000_000
    else:
        over_million = 0
        under_million = gross_salary

    # 税額の計算（小数点第一位を四捨五入）
    tax_amount = round((over_million * tax_rate_over_million) + (under_million * tax_rate_under_million))
    
    # 支給額の計算
    net_salary = round(gross_salary - tax_amount)

    return net_salary, tax_amount

# 給与額の入力
gross_salary = float(sys.argv[1])

# 税額と支給額の計算
net_salary, tax_amount = calculate_tax_and_net_salary(gross_salary)

print(f"支給額:{net_salary}、税額:{tax_amount}",end="")


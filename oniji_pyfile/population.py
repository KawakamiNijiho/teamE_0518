import sys
args = sys.argv
num = int(args[1])

# タプル population を作成
population = (
    "China",
    "India",
    "U.S.A",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russia",
    "Mexico"
)

# 引数に指定した順位の国名を出力
print(population[num-1], end="")
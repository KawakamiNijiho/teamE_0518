import sys
args = sys.argv

# コマンドライン引数から値下げ対象の種類と値下げ額を取得
type = args[1]
price_down = int(args[2])

# 価格表の定義
price_table = {
        "リンゴ": 80,
        "みかん": 198,
        "バナナ": 150,
        "ビール": 360,
        "日本酒": 580,
        "ラーメン": 380,
        "うどん": 128,
        "パスタ": 258
}

fruits = ("リンゴ", "みかん", "バナナ") 
alcohol = ("ビール", "日本酒")  
noodles = ("ラーメン", "うどん", "パスタ")

if type == "麺類":
    check = noodles
elif type == "酒類":
    check = alcohol
elif type == "果物類":
    check = fruits
    

# 値下げ対象の価格表を更新
for item in price_table.keys():
    if item in check:
        price_table[item] = max(1, price_table[item]- price_down)

print(price_table,end="")
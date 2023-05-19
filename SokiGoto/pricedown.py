import sys
args = sys.argv

# 引数を変数に代入
hm_class = args[1]  # 値下げ対象の種別
price_down = int(args[2])  # 値下げ額

# 品目（品名と価格）を辞書型で定義
hinmoku = {
    "リンゴ": 80,
    "みかん": 198,
    "バナナ": 150,
    "ビール": 360,
    "日本酒": 580,
    "ラーメン": 380,
    "うどん": 128,
    "パスタ": 258
    }

# 区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")  # 果物類をタプルで定義
alcohol = ("ビール", "日本酒")  # 酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")  # 麺類をタプルで定義

# 値下げの種別によって判定するタプルを選ぶ
if hm_class == "麺類":
    check = noodles
elif hm_class == "酒類":
    check = alcohol
elif hm_class == "果物類":
    check = fruits

# 品目をkeyで回す
for label in hinmoku.keys():
    # 品目名がcheckの中にあれば値段を下げる
    if label in check:
        hinmoku[label] = max(0, hinmoku[label] - price_down)

# 品目の結果を出力する
print(hinmoku, end="")

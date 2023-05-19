import sys
args = sys.argv
hm_class = args[1]
price_down = int(args[2])

# 価格表を辞書型で定義
hinmoku = {
    "リンゴ":80 ,
    "みかん":198, 
    "バナナ":150, 
    "ビール":360, 
    "日本酒":580, 
    "ラーメン":380, 
    "うどん":128, 
    "パスタ":258
    }

#区分ごとの定義
#果物類をタプルで定義
fruits = ("リンゴ", "みかん", "バナナ")          
#酒類をタプルで定義
alcohol = ("ビール", "日本酒")
#麺類をタプルで定義                         
noodles = ("ラーメン", "うどん", "パスタ") 

# 第二引数が果物類の場合、果物類の価格から第三引数の値を引く
if hm_class == "果物類":
    for i in fruits:
        hinmoku[i] = hinmoku[i] - price_down
        if hinmoku[i] < 1:
            hinmoku[i] = 1

# 第二引数が酒類の場合、果物類の価格から第三引数の値を引く
if hm_class == "酒類":
    for i in alcohol:
        hinmoku[i] = hinmoku[i] - price_down
        if hinmoku[i] < 1:
            hinmoku[i] = 1

# 第二引数が麺類の場合、果物類の価格から第三引数の値を引く
if hm_class == "麺類":
    for i in noodles:
        hinmoku[i] = hinmoku[i] - price_down
        if hinmoku[i] < 1:
            hinmoku[i] = 1

print(hinmoku)

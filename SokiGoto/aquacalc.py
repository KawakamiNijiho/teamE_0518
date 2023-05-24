import sys
import datetime

# 引数を受け取る
day = sys.argv[1]
number_of_adult = int(sys.argv[2])
number_of_children = int(sys.argv[3])
# 平日と休日,大人と子供の料金を定義する
fee = {
    ("weekday", "adult"): 2000,
    ("weekday", "children"): 1200,
    ("holiday", "adult"): 2400,
    ("holiday", "children"): 1500
    }
# 日付が平日か休日か判断する
dt = datetime.date(int(day[:4]), int(day[4:6]), int(day[6:]))
week_day = dt.weekday()
if week_day >= 5:
    week_day_char = "holiday"
else:
    week_day_char = "weekday"
# 人数に料金をかけて合計を求める
ans = fee[(week_day_char, "adult")] * number_of_adult + fee[(week_day_char, "children")] * number_of_children
# 合計の料金を出力する
print(ans, end="")

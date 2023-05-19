# import module
import sys
args = sys.argv
# set 変数
sta1 = args[1]
sta2 = args[2]
distance = 0

# make dictionary
station = {
    '東京':0.00,
    '品川':6.78,
    '新横浜':25.54,
    '名古屋':342.02,
    '京都':476.31,
    '新大阪':515.35
}

# 計算して四捨五入して表示
distance = round(abs(station[sta2] - station[sta1]),2)



print(distance, end="")
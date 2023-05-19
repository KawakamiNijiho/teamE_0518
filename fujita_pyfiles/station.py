#モジュールインポート
import sys

#引数受取
args=sys.argv
station_1=str(args[1])
station_2=str(args[2])

#辞書定義
dist_dict={"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}

#距離計算
dist=round(abs(dist_dict[station_2]-dist_dict[station_1]),2)

#出力
print(dist,end="")
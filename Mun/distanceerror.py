import sys

station = sys.argv
select = station[1:]

try:
    stations = {'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}
    print(round(stations[select[0]]-stations[select[1]],2),end="")
except:   
    print("のぞみの停車駅を引数に設定してください",end="")

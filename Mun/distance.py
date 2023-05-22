import sys

station_name = sys.argv

stations = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02,"京都":476.31,"新大阪":515.35}

if stations[station_name[1]] < stations[station_name[2]]:
    distance = (stations[station_name[2]] - stations[station_name[1]])
else:
    distance = (stations[station_name[1]])-(stations[station_name[2]])

print(round(distance,2),end="")

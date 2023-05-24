from datetime import date,sys
from database import session
from tables import Holiday

args = sys.argv


year = int(args[1][0:4])
month = int(args[1][4:6])
day = int(args[1][6:8])

dt = date(year, month, day)

holidays = session.query(Holiday.holi_date).filter_by(holi_date=dt).all()

print(holidays)

if holidays is not None:
    print("Today is holiday")
else:
    print("Today is Workday")

# weekday = dt.strftime("%a")

# #old[0] = 平日 old[1] = 週末
# old = (2000,2400) 
# young = (1200,1500)


# #args[2] = 大人 args[3] = 子供
# if weekday == "Sat" or weekday == "Sun":
#     sum = (int(args[2])*old[1]) + (int(args[3])*young[1])
# else:
#     sum = (int(args[2])*old[0]) + (int(args[3])*young[0])

# print(sum,end="")
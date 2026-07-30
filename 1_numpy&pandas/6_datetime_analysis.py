import datetime as dt
dt1=dt.datetime(2025,12,31)
print(dt1)

thursday_list=[]
current_day=dt.datetime(2026,1,1)
d1=dt.timedelta(days=1)
for i in range(365):
    current_day=current_day+d1
    print(current_day)
    if current_day.weekday()==3:
        thursday_list.append(current_day)
        print(current_day)

print(thursday_list)
print(len(thursday_list))

    
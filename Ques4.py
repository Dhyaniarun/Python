import datetime
dd1 = input("Enter the date in dd format")
mm1 = input("Enter the month in mm format")
yy1 = input("Enter the year in yyyy format")
dd2 = input("Enter the date in dd format")
mm2 = input("Enter the month in mm format")
yy2 = input("Enter the year in yyyy format")
date1=datetime.date(yy1,mm1,dd1)
date2=datetime.date(yy2,mm2,dd2)
diff=date1-date2
print diff

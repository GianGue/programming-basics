year, month, day=input('Please insert year, month and day divided by sign - (ex. 2020-10-01): ').split('-')
year=int(year)
month=int(month)
day=int(day)
month_31 = [1,3,5,7,8,10]
month_30 = [4,6,9,11]
#str(1).zfill(2)
if day == 31 and month == 12 :
    print((year+1),'-','01','-','01',sep='')
elif day == 31 and month in month_31:
    print(year,'-',(str(month+1).zfill(2)),'-','01',sep='')
elif day == 30 and month in month_30:
    print(year,'-',(str(month+1).zfill(2)),'-','01',sep='')
elif ((year)%400)==0:
    if ((year)%100)==0 and month == 2 and day == 28:
        print(year,'-',(str(month+1).zfill(2)),'-','01',sep='')
elif ((year)%4)==0 and month == 2 and day == 29:
    print(year,'-',(str(month+1).zfill(2)),'-','01',sep='')
else:
    print(year,'-',(str(month).zfill(2)),'-',(str(day+1).zfill(2)),sep='')

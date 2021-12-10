year=int(input('Please insert a year: '))

if (int(year)%400)==0:
    if (int(year)%100)==0:
        print('This year is a not leap year!')
    else:
        print('This year is a leap year!')
elif (int(year)%4)==0:
    print('This year is a leap year!')
else:
    print('This year is not a leap year!')



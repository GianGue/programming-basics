year=int(input('Please insert an year: '))
day_of_the_week = (year + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)) % 7

if day_of_the_week == 0:
    print('The first day of the week is Sunday!')
elif day_of_the_week == 1:
    print('The first day of the week is Monday!')
elif day_of_the_week == 2:
    print('The first day of the week is Tuesday!')
elif day_of_the_week == 3:
    print('The first day of the week is Wednesday!')
elif day_of_the_week == 4:
    print('The first day of the week is Thursday!')
elif day_of_the_week == 5:
    print('The first day of the week is Friday!')
elif day_of_the_week == 6:
    print('The first day of the week is Saturday!')
#request number of seconds from user
x = int(input("Please insert your total amount of seconds: "))
#divide amount of seconds in days,hours,minutes and seconds
#day=86400, hour=3600, minutes=60 
day = int(x / 86400)
day_rest = x % 86400
hour = int(day_rest / 3600)
hour_rest = day_rest % 3600
mins = int(hour_rest / 60)
mins_rest = hour_rest % 60
sec = int(mins_rest)
print("Your total amount of days, hours, minutes and seconds is: ") 
print(str(day).zfill(2),':',str(hour).zfill(2),':',str(mins).zfill(2),':',str(sec).zfill(2))

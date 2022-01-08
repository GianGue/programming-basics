charge = 0

while True:
    age = input('Please insert age of any single component of the group: ')

    if age == ' ':
        print(f"Total charge is: ${charge:.2f}")
        break

    if int(age) <= 2:
        charge = 0
    elif 3 <= int(age) <= 12:
        charge += 14.00
    elif int(age) >= 65:
        charge += 18.00
    else:
        charge += 23.00


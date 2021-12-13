SENTINEL = 0
num = []
while True:
    num = [int(num) for num in input('Please insert values divided by a space, use 0 to terminate: ').split()]

    if num[0] == SENTINEL:
        print("Error: please don't insert 0 like first number")
        break

    if SENTINEL in num:
        average = sum(num)/(len(num) - num[SENTINEL])
        print(f'Average of number insered is: {average:.2f}')
        break

    if SENTINEL not in num:
        print("Error: please insert 0 after list of numbers!")
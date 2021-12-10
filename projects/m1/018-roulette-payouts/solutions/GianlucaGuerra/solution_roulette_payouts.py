name=input('Please insert your name: ')
red_number = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black_number = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green_number = [0,00]
total_numbers = [0,00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
import random
result_number = random.choice(total_numbers)
print('Well',name+',','the spin resulted in:',result_number)
if result_number in green_number:
    if result_number == 0: 
        print('Pay 0')
    elif result_number == 00:
        print('Pay 00')
elif result_number in red_number:
    print('Pay', result_number)
    print('Pay Red')
    if (result_number % 2) == 1: 
      print('Pay Odd')
    elif (result_number % 2) == 0:
        print('Pay Even')
    if result_number >= 1 and result_number <= 18:
        print('Pay 1 to 18')
    elif result_number >= 19 and result_number <= 36:
        print('Pay 19 to 36')
elif result_number in black_number:
    print('Pay', result_number)
    print('Pay Black')
    if (result_number % 2) == 1: 
      print('Pay Odd')
    elif (result_number % 2) == 0:
        print('Pay Even')
    if result_number >= 1 and result_number <= 18:
        print('Pay 1 to 18')
    elif result_number >= 19 and result_number <= 36:
        print('Pay 19 to 36')

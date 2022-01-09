while True:
 
    bits = input('Please insert a total amount of 8 bits:')
    count_bits = bits.count('1')
    if bits == ' ':
        print('Thank you for your collaboration, bye!')
        break
    elif len(bits) > 8:
        print('Please insert a total of 8 bits!')
        
    elif count_bits % 2 == 1:
        print('Your parity should be 0')
        continue
    elif count_bits % 2 == 0:
        print('Your parity should be 1')
        continue
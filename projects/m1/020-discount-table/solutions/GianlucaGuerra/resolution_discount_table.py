#discount 60% off
prices = [4.95, 9.95, 14.95, 19.95, 24.95]
#discount = prices - ((prices*6)/10)
for price in prices:
    discount = price - ((price*6)/10)
    print('\nOriginal price is ', str(price),'$')
    print(f'Discount amount is {((price / 10) * 6):.2f}$')
    print(f'New total price is {discount:.2f}$')


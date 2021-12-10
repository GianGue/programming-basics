minutes = float(input('Please inset the amount of minutes made: '))
messages = float(input('Please insert the amount of messages sent: '))
call911 = float(input('Please insert call made to 911: '))

if minutes >= 50:
  tot_min = (minutes - 50)*0.25
else:
    tot_min = minutes*0
if messages >= 50:
   tot_mex = (messages - 50)*0.15 
else:
    tot_mex = messages*0
tot_call911 = call911*0.44
tax_add = ((tot_min+tot_mex+tot_call911)*5)/100

print('Base charge is : 15 euro')
print('Additional minutes charge (if applicable): ', float('%.2f' %tot_min), 'euro')
print('Additional messages charge (if applicable): ', float('%.2f' %tot_mex), 'euro')
print('Call to 911 charge (if applicable): ', float('%.2f' %tot_call911), 'euro')
print('Total tax: ', float('%.2f' %tax_add), 'euro')
print('Total bill amount: ', 15 + ((float('%.2f' %tot_min) + float('%.2f' %tot_mex) + float('%.2f' %tot_call911)) + float('%.2f' %tax_add)), 'euro')
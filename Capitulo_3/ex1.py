hours = input('Enter the hours: ')
rate = input('Enter the rate: ')
try:
    if int(hours)>40:
        pay = int(hours)*(int(rate)*1.5)
    else:
        pay = int(hours)*int(rate)
    print('Pay: ' + str(pay))

except:
    print('Please enter a number')
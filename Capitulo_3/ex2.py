try:
    hours = input('Enter the hours: ')
    a = int(hours)
    rate = input('Enter the rate: ')
    b = int(rate)
    if a>40:
        pay = a*(b*1.5)
    else:
        pay = a*b
    print('Pay: ' + str(pay))

except:
    print('Error, please enter a numeric input')
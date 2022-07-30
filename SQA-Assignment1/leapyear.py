def isLeapYear(year):
    
    if (year % 400 == 0) and (year % 100 == 0):
        return "It is a leap year!"

    elif (year % 4 ==0) and (year % 100 != 0):
        return "It is a leap year!"

    else:
        return "It is not a leap year!!"
   

'''
print(isLeapYear(2024))
print(isLeapYear(2032))
print(isLeapYear(1999))
'''   

def nextDay(year, month, day):
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
    
def isLeapYear(year):
    if year%400==0:
        return True
    else:
        if year%100==0:
            return False
        else:
            if year%4==0:
                return True
            else:
                return False
        
def daysInMonth(year,month):
    if month == 1 or month ==3 or month ==5 or month ==7 or \
    month ==8 or month ==10 or month ==12:
        return 31
    else:
        if month == 4 or month ==6 or month ==9 or month ==11:
            return 30
        else:
            if isLeapYear(year):
                return 29
            else:
                return 28

print (daysBetweenDates(1900,1,1,1901,12,31))
print (daysBetweenDates(2012,1,1,2012,2,28))
print (daysBetweenDates(2012,1,1,2012,3,1))
print (daysBetweenDates(2011,6,30,2012,6,30))
print (daysBetweenDates(2011,1,1,2012,8,8))
print (daysBetweenDates(1900,1,1,1999,12,31))

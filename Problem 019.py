#Counting the number of months with Sunday as the first of the month from Jan 1901 to Dec 2000
sundayfirst = 0
thirtydaymonths = [4, 6, 9, 11]
year = 1901
day = 0
while year < 2001:
    month = 1
    while month <= 12:
        #1 Jan 1901 was a Tuesday, so Sundays are when daycount mod 7 is 5
        if day % 7 == 5:
            sundayfirst += 1
        #Sorting out leap years
        if month == 2:
            if (year % 4 == 0) and (year % 100 != 0):
                day += 29
            elif (year % 100 == 0) and (year % 400 == 0):
                day += 29
            else:
                day += 28
        elif month in thirtydaymonths:
            day += 30
        else:
            day += 31
        month += 1
    year += 1
    
print(sundayfirst)
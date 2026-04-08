year = 2004
year_isLeap = (year%4) == 0 
if year_isLeap:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

#Sir Approach
year = 2023

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year")
else:
    print(year, "is NOT a leap year")
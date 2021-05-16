#!/usr/bin/env python
# coding: utf-8




year = int(input("Enter a year to check if year is a leap year or not: "))
def year_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
    
year_leap(year)


    











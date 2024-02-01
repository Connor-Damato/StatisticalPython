#!/usr/bin/python3
from re import A


n = 21
# Your code should be below this line

def isWeekend(dayOfJanuary):
    if (dayOfJanuary < 1 or dayOfJanuary > 31):
        print("Not valid")
    elif ((dayOfJanuary - 1) % 7 < 2):
        print("Weekend")
    else:
        print("Weekday")

isWeekend(n)
#!/usr/bin/python3
from math import sqrt
from tkinter import Place
from turtle import end_fill


number = 100
# Your code should be below this line

def checkInFibbonacci(sampleNum):
    if (sampleNum <= 0 or sampleNum % 2 == 1):
        print("No")
    elif (sqrt((5 * (sampleNum ** 2) - 4)) % 1 == 0):
        print("Yes")
    elif (sqrt((5 * (sampleNum ** 2) + 4)) % 1 == 0):
        print("Yes")
    else:
        print("No")

checkInFibbonacci(number)
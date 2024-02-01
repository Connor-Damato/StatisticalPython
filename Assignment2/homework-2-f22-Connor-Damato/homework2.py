from typing import Tuple


def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here
    hist = []

    if (b == h):
        print("b and h are the same value")
    if (b > h):
        tempVal = b
        b = h
        h = tempVal
    if (b < h):
        for bin in range(n):
            hist.append(0)

        dataSet = set()
        for point in data:
            if (point > b and point < h):
                dataSet.add(point)

        w = (h - b) / n
        for bin in range(n):
            lowerBound = b + bin * w
            upperBound = b + (bin + 1) * w
            for j in dataSet:
                if (j >= lowerBound and j < upperBound):
                    hist[bin] += 1
    # return the variable storing the histogram
    # Output should be a list
    return hist
    pass


def happybirthday(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    
    # Write your code here
    date_to_all = {}
    for name, day in name_to_day.items():
        month = name_to_month[name]
        year = name_to_year[name]
        age = 2022 - year
        if day in date_to_all:
            if (age > date_to_all[day][1][2]):
                date_to_all[day] = (name, (month, year, age))
        else:
            date_to_all[day] = (name, (month, year, age))
    # return the variable storing date_to_all
    # Output should be a dictionary
    return date_to_all
    pass


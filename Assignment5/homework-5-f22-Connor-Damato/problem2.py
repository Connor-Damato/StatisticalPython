import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32, 10, -4]

# code for question 1
print('Problem 1 Answers:')
# code below this line
sampleSize = len(data)
sampleMean = sum(data) / sampleSize
print("mean:", sampleMean)
SE = np.std(data, ddof=1) /  (sampleSize ** .5)
print("SE:", SE)
t_c = stats.t.ppf(1-(1-.9)/2, df = sampleSize - 1)
print("Standard Stat:", t_c)
upper = sampleMean + t_c * SE
lower = sampleMean - t_c * SE

print("Lower: ", lower)
print("Upper: ", upper)


# code for question 2
print('\nProblem 2 Answers:')
# code below this line
t_c = stats.t.ppf(1-(1-.95)/2, df = sampleSize - 1)
print("Standard Stat:", t_c)
upper = sampleMean + t_c * SE
lower = sampleMean - t_c * SE

print("Lower: ", lower)
print("Upper: ", upper)

# code for question 3
print('\nProblem 3 Answers:')
# code below this line
SE = 15.836/(sampleSize ** .5)
z_c = stats.norm.ppf(1-(1-.95)/2)
print("SE :", SE)
print("Standard Stat:", z_c)

lower = sampleMean - z_c * SE
upper = sampleMean + z_c * SE

print("Lower: ", lower)
print("Upper: ", upper)

# code for question 4
print('Problem 4 Answers:')
# code below this line
SE = np.std(data, ddof=1) / (sampleSize ** .5)
c = 2* stats.t.cdf(sampleMean / SE, df = sampleSize - 1) - 1
print("Confidence:", c)

import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset herex
myFile = open("engagement_1.txt")
data = myFile.readlines()
myFile.close()

data = [float(x) for x in data]

# code for question 2
print('Problem 2 Answers:')
# code below this line
trueMean = 0.75
sampleSize = len(data)
print("Sample Size:", sampleSize)

sampleMean = sum(data) / sampleSize
print("Sample Mean:", sampleMean)

standardDeviation = np.std(data, ddof = 1)
print("Standard Deviation:", standardDeviation)
standardError = (standardDeviation)/(sampleSize ** 0.5)
print("Standard Error:", standardError)

zScore = ((sampleMean - trueMean) / standardError)
print("Standard Score:", zScore)

pValue = 2 * stats.norm.cdf(-abs(zScore))
print("p-value:", pValue)

# code for question 3
print('\nProblem 3 Answers:')
# code below this line
seOfAlpha = (sampleMean - trueMean) / stats.norm.ppf(0.025)
print("SE:", seOfAlpha)

nOfAlpha = (standardDeviation / seOfAlpha) ** 2
print("Corresponding N:", nOfAlpha)

# code for question 5
print('\nProblem 5 Answers:')
# code below this line
myFile = open("engagement_0.txt")
data2 = myFile.readlines()
myFile.close()

data2 = [float(x) for x in data2]

standardDeviation2 = np.std(data2, ddof = 1)
print("Standard Deviation:", standardDeviation2)
sampleSize2 = len(data2)    
sampleMean2 = sum(data2)/sampleSize2
print("Sample Size:", sampleSize2)
print("Mean:", sampleMean2)

deviation = (((standardDeviation ** 2) / sampleSize) + ((standardDeviation2 ** 2) / sampleSize2)) ** 0.5
print("Standard Error:", deviation)
z_score = (sampleMean2 - sampleMean) / deviation
print("Standard Score:", z_score)

print("pValue:", 2 * stats.norm.cdf(-abs(z_score)))

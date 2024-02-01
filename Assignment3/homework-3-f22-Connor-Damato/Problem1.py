from xml.dom import HierarchyRequestErr
import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    output a histogram of probabilities(list) and a sum of the histogram of counts, i.e. the number of samples(int)
    :param hist: a numpy ndarray object
    :return: a tuple that contains a list and a int, i.e. ([...], int)
    """
    # please delete the "pass" below and your code starts here...
    probs = []
    total = sum(hist)
    for bin in hist:
        probs = probs + [bin / total]
    return (probs, total)


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram function to output the histogram of probabilities and the number of samples, 
    then calculates compute_j for one bin width (reference: histogram.pdf page19)
    :param histo: list
    :param width: float
    :return: float
    """
    # please delete the "pass" below and your code starts here...
    probs = norm_histogram(histo)
    return (2/ ((probs[1] - 1) * width)) - ((probs[1] + 1)/ ((probs[1] - 1) * width)) * sum(list(map(lambda x: x**2,probs[0])))


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    
    The variable "data" is the raw data that still needs to be "processed"
    with matplotlib.pyplot.hist to output the histogram

    You need to utilize the variables (data, minimum, maximum, min_bins, max_bins) 
    in sweep_n functions to give values to (x, bins, range) in the function matplotlib.pyplot.hist
    Other input variables of matplotlib.pyplot.hist can be set as default value.
    
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    # please delete the "pass" below and your code starts here...
    jVals = []
    for width in range(min_bins, max_bins + 1):
        hist, binwidth = plt.hist(data, width, (minimum, maximum))[0:2]
        jVals.append(compute_j(hist, binwidth[1] - binwidth[0]))
    return jVals


def find_min(l):
    """
    takes a list of numbers and returns the two smallest number in that list and their index.
    return as a dict i.e. 
    {index_of_the_smallest_value: the_smallest_value, index_of_the_second_smallest_value: the_second_smallest_value}
    
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        Then you should return {0: 14, 2: 15}

    :param l: list
    :return: dict
    """
    # please delete the "pass" below and your code starts here...
    minVal = min(l)
    minLocation = l.index(minVal)
    l.pop(minLocation)
    secondVal = min(l)
    secondLocation = l.index(secondVal)
    if (secondLocation >= minLocation):
        secondLocation += 1
    return {minLocation: minVal, secondLocation: secondVal}


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))

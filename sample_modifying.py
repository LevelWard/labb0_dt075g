import numpy as np


def spliceSample(samples_array, start, end):
    # takes in args 'samples_array', 'start', 'end'
    # returns spliced array
    spliced_array = samples_array[start:end]
    return spliced_array


def sumOfSamples(a, b):
    # takes in args a & b, which are samples of array
    sum_array = np.add(a, b)
    return sum_array

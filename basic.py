import numpy as np
import math


def formatPrice(n):
    return("-Rs." if n<0 else "Rs.")+"{0:.2f}".format(abs(n))
def getStockDataVec(key):
    vec = []
    lines = open(key+".csv","r").read().splitlines()
    counter = 1
    for line in lines[1:]:
        #print(line)
        #print(float(line.split(",")[4]))

        vec.append(float(line.split(",")[4]))

        #print(vec)
    return vec
def sigmoid(x):
    return 1/(1+math.exp(-x))
def getState(data, t, n):
    d = t - n + 1
    block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0
    res = []
    for i in range(n - 1):
        res.append(sigmoid(block[i + 1] - block[i]))
    return np.array([res])
from chpt5_statistics import *
from math import pi,exp,erf
from random import random

def uniform_pdf(x):
    return 1 if x >= 0 else 0

def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

def norm_pdf(x,mu=0,sigma=1):
    sqrt_two_pi = sqrt(2 * pi)
    return (exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x,mu,sigma):
    return (1 + erf(x - mu) / sqrt(2) / sigma)

def invers_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
    if my != or sigma != 1:
        return mu + sigma *  inverse_normal_cdf(p,tolerance=tolerance)
    lo_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            lo_z = mid_z
        elif mid_p > p:
            hi_z = mid_z
        else:
            break
    return mid_z

def bernoulli_trial(p):
    return 1 if random() < p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

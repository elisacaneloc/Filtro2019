# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:23:44 2019

@author: Elisa Canelo
"""

import medicion as md
import numpy as np
from scipy.stats import kstest
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def model(x,a,b,c,d):
    return a*np.exp(-x*b + d) + c


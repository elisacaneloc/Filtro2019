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

# copiemos para uno y después lo arreglamos para todos
# y despues hacemos función.
    

def reducir(D_i,C_i):
    x_data = D_i
    y_data = C_i
    n = len(x_data)
    data = np.zeros(n,2)
    for i in range(n):
        data[i][0] = x_data[i]
        data[i][1] = y_data[i]
    
    data_quiero = []
    for i in range(n):
        if 2>data[i][0]>0:
            data_quiero.append(data[i])
    data_quiero = np.array(data_quiero)
    s = len(data_quiero)
    y_data_quiero = np.zeros(s)
    x_data_quiero = np.zeros(s)
    for i in range(s):
        x_data_quiero[i] = data_quiero[i][0]
        y_data_quiero[i] = data_quiero[i][1]
    return x_data_quiero, y_data_quiero


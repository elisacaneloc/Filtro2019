# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:53:26 2019

@author: NACHO
"""

import numpy as np
#from sklearn import preprocessing, model_selection, neighbors
#import pandas as pd
#import csv
import re


#filename='G:/curcuminoids/MeSPh-BF2/sample 7/15-19/molecule/scan161104_62_0.dat'

#data= pd.read_csv('G:/curcuminoids/MeSPh-BF2/sample 7/15-19/molecule/scan161104_62_0.dat', delimiter= '\t', skiprows=range(14), header=None, names=['time', 'G', 'bin'])
def readtrace(filename) : 
    with open(filename) as file:
        lines = [line.strip() for line in file]
        
    start=lines.index("@")
    endb=lines.index("@",start+1)
    
    T=[]
    G=[]
    
    for ll in lines[start+1:endb-1]:
        T.append(float(ll.split("\t")[0]))
        G.append(float(ll.split("\t")[1]))
    
    s=[ s for s in lines[:start] if "Breaking speed 2 :" in s]
    speed=  float(re.search(r'Breaking speed 2 :(.*?) V/s',s[0]).group(1))
    s=[ s for s in lines[:start] if "set voltage :" in s]
    V=float(re.search(r'set voltage :(.*?) V',s[0]).group(1))
    
    return T, G, V, speed
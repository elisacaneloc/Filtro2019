#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
from scipy import io

'''
Este programa está pensado para trabajar con los datos del archivo curves.mat
La idea es poder hacer lo mismo que está hecho en el programa de matlab pero
pero en python.
'''

curve = sp.io.loadmat('curves.mat')
curve_cell = curve['curva_cell']

todos_y = []
for i in range(0,5000):
    datos = curve[0,i]
    d = datos[0][0]
    y = d[1]
    todos_y.append(y)

todos_x = []
for i in range(0,5000):
    datos = curve[0,i]
    d = datos[0][0]
    x = d[1]
    todos_x.append(x)

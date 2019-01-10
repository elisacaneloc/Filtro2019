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
# Parametros

trazas = 5000 # numero de trazas de los datos
cali = 0.02

# leemos el archivo

curve = sp.io.loadmat('curves.mat')
curve_cell = curve['curva_cell']

'''
Juntamos todos los y de todas las trazas en una sola lista de python
se puede acceder a cada traza como en una lista.
'''

todos_y = []
for i in range(0,trazas):
    datos = curve[0,i]
    d = datos[0][0]
    y = d[1]
    todos_y.append(y)

'''
Juntamos todos los x de todas las trazas en una sola lista de python
se puede acceder a cada traza como en una lista.
'''

todos_x = []
for i in range(0,trazas):
    datos = curve[0,i]
    d = datos[0][0]
    x = d[0]
    todos_x.append(x)

# renombramos todos_y como allConduct
allConduct = todos_y

allDisplace = []
for i in range(len(todos_x):
    displace = todos_x[i]*2
    allDisplace.append(displace)

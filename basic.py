#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Implementación de un nuevo método de filtrado
'''

# importamos
import scipy as sp

'''
Leemos los archivos .mat para trabajar con ellos como array de scipy
'''

allconduct = sp.io.loadmat('allConduct.mat')
alldisplace = sp.io.loadmat('allDisplace.mat')

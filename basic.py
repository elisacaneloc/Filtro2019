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

'''
Ahora seleccionamos del archivo solo la parte que nos interesa
pues si uno ve el contenido de este, vera que hay muchas cosas
que no nos sirven, con esto podremos usar su contenido como
un array normal, recordemos que en python la idenxacion parte en 0
por lo tanto tenemos desde la traza 0 (1) hasta la 4999 (5000)
'''

allconduct = allconduct['allConduct']
alldisplace =  alldisplace['allDisplace']

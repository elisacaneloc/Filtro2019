# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:23:44 2019

@author: Elisa Canelo

En este script están todas las funciones necesarias
para poder filtrar los datos desde que uno ya extrajo lo datos anteriormente
"""

import medicion as md
import numpy as np
from scipy.stats import kstest
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def model(x,a,b,c,d):
    '''
    model define el modelo exponencial con el que fitearemos nuestros datos
    resive un array y retorna un array transformado por la exponenecial
    definido por los parametros libres.
    
    La exponencial es de la forma
            a * np.exp(-x * b + d) +c 
        Parameters
        --------------
        x :         array
                        vector de datos a transformar
        a, b, c, d: num
                        parametros que pueden ser entregados de a uno o en un
                        vector. Pueden ser enteros, float o complejos. Son li_
                        bres. 
                            a: Es el parametro que multiplica la exponencial.
                            b: multiplica la variable dentro de la exponencial.
                            c: parametro que se suma dentro de la exponencial.
                            d: parametro que se suma a la exponencial.
        Returns
        --------------
        y : array
                    array al que se le aplico la transformación.
    '''
    return a*np.exp(-x*b + d) + c

    

def reducir(D_i,C_i):
    '''
    Funcion que permite achicar los vectores con los que trabajaremos luego en
    el filtrado de los datos. Esto ayuda a que el fit sea mejor ya que los
    datos fuera del rango, no son modelables con la exponencial. 
    Esta función está hecha para seleccionar los datos de solo una traza.
    Selecciona los datos para los desplazamientos entre 0 y 2.
        Parameters:
        -------------
        D_i: np.array
                        Vector de desplazamientos de una traza
        C_i: np.array
                        Vector de conductancias de una traza
        Returns:
        ------------
        x_data_quiero: array
                                Vector que contiene los desplazamientos
                                seleccionados.
        y_data_quiero: array
                                Vector que contiene las conductancias seleccio_
                                nadas.
    '''
    x_data = D_i
    y_data = C_i
    n = len(x_data)
    data = np.zeros(n,2)
    # juntamos los datos en una sola matriz para que así al seleccionarlos,
    # ambos queden con la misma cantidad de datos.
    for i in range(n):
        data[i][0] = x_data[i]
        data[i][1] = y_data[i]
    # ahora seleccionamos los datos 
    data_quiero = [] # lista que contrendá los pares seleccioandos
    for i in range(n):
        if 2>data[i][0]>0: # filtro seleccionador
            data_quiero.append(data[i])
    data_quiero = np.array(data_quiero) # transformamos la lista en un array
    s = len(data_quiero)
    # nuevamente separamos los datos en dos vectores para retornarlos separados
    y_data_quiero = np.zeros(s)
    x_data_quiero = np.zeros(s)
    for i in range(s):
        x_data_quiero[i] = data_quiero[i][0]
        y_data_quiero[i] = data_quiero[i][1]
    return x_data_quiero, y_data_quiero


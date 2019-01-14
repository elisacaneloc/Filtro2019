# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:40:48 2019

@author: Elisa Canelo
"""

import numpy as np
import re

def readtrace(filename):
     with open(filename) as file:
        lines = [line.strip() for line in file]
        
        start=lines.index("@")
        endb=lines.index("@",start+1)
    
        T=[] # tiempo
        C=[] # conductancia
    
        for ll in lines[start+1:endb-1]:
            T.append(float(ll.split("\t")[0]))
            C.append(float(ll.split("\t")[1]))
            
            s=[ s for s in lines[:start] if "Breaking speed 2 :" in s]
            speed=  float(re.search(r'Breaking speed 2 :(.*?) V/s',s[0]).group(1))
            s=[ s for s in lines[:start] if "set voltage :" in s]
            Vbias=float(re.search(r'set voltage :(.*?) V',s[0]).group(1))
        
        V_p = [t*speed for t in T]
        C_index = tuple(enumerate(C))
        C0 = [c for c in C_index if c[1]>0.75][-1]
        V_0 = V_p[C0[0]]
        D = [vp - V_0 for vp in V_p]
        return np.array(D), np.array(C), Vbias, speed

def readmeasure(cadena, trazas):
    '''
    Función que genera a partir de una ruta generica y el numero de trazas, 
    el resultado de toda la medición. Usa readtrace para leer cada traza,
    para luego guardar cada T y C en una lista, los que luego se ordenan en
    un array. 
        Parameters    
        ----------------------------
        cadena: string
                        ruta generico de los .dat donde el formato es 
                        "C:\....\scanXXXXX_X_{0}.dat" donde los X son los que
                        correspondan para cada medición.
        trazas: int 
                        numero de trazas de la medición
        
        Returns
        --------------------------
        D_measure : List
                        Lista de arrays que contienen los desplazamientos para
                        cada traza.
        
        C_measure : List
                        Lista de arrays que contiene las conductancias para
                        cada traza.
                        
        Vbias :  num
                        Numero que corresponde al voltaje de la medición
                        
        Speed: num
                        Numero que corresponde a la velocidad de la medición 
    '''
    C_measure = []
    D_measure = []
    for i in range(trazas):
        cadena_format = cadena.format(i)
        D, C, Vbias, Speed = readtrace(cadena_format)
        C_measure.append(C)
        D_measure.append(D)
    return D_measure, C_measure, Vbias, Speed 

    





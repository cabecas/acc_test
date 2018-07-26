# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:23:22 2018

@author: ferna
"""

import numpy as np
import acc


def select_entire_pulse(mat, set_point1 = 0.2, set_point2 = -3,
                        shift=50):
    i = 0
    t = []
    pH = []

    while mat.shape[0] > i:
        while set_point1 >= mat[i, 2]:
            print(i)
            i = i + 1

    
        t = np.append(t, mat[i, 0])
        pH = np.append(pH, mat[i, 1])
    
        while mat[i, 2] >= set_point2:
            t = np.append(t, mat[i, 0])
            pH = np.append(pH, mat[i, 1])
            i = i + 1
            print(i)
            if i == mat.shape[0]:
                break

    return t, pH

            
    '''
    t = []
    pH = []
    
    for i in np.arange(mat.shape[0]):
        if mat[i, 2] > set_point1:
            t = np.append(t, mat[i, 0])
            pH = np.append(pH, mat[i, 1])
            try:
                while mat[i, 2] > set_point2:
                    t = np.append(t, mat[i+1, 0])
                    pH = np.append(pH, mat[i+1, 1])
                    i = i + 1
                    print(i)
            except:
                break

    return t, pH
    '''

mat = acc.read_file('pH412.test', 'Folha4')
clean = acc.cleaning(mat, analise='pH')
slopes = acc.declive(clean, window=100)

t1,pH1 = select_entire_pulse(slopes)
all_pulses = acc.breaking(t1, pH1)
#all_pulses = acc.breaking2(all_pulses)
acc.plotting(all_pulses)

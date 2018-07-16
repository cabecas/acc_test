# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:23:22 2018

@author: ferna
"""

def select_entire_pulse(mat, set_point1=0.2, set_point2=-3, shift=50):

    '''
    i = 0
    t = []
    pH = []
    
    
    
    while mat[i,2] <= set_point1:
        i = i+1
    
    t=np.append(t, mat[i, 0])
    pH=np.append(pH, mat[i, 1])
    
    while mat[i,2] >= set_point2 and i < len(mat):
            t=np.append(t, mat[i, 0])
            pH=np.append(pH, mat[i, 1])
            i= i+1
            print(i)
            
    '''
    
    t=[]
    pH=[]
    
    for i in np.arange(mat.shape[0]):
        if mat[i,2] > set_point1:
            t=np.append(t, mat[i, 0])
            pH=np.append(pH, mat[i, 1])
            try:
                while mat[i,2] > set_point2:
                    t=np.append(t, mat[i+1, 0])
                    pH=np.append(pH, mat[i+1, 1])
                    i = i+1
                    print(i)
            except:
                break
    
               
    return t, pH



t1,pH1=select_entire_pulse(slopes)
all_pulses=breaking(t1,pH1)
all_pulses=breaking2(all_pulses)
plotting(all_pulses)

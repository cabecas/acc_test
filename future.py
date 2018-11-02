# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:23:22 2018

@author: ferna
"""

import numpy as np
from numpy.core.multiarray import ndarray
import scipy.signal  # It requires scipy version 1.1.0
import acc
import matplotlib.pyplot as plt


def indices_max(mat, cut_value=1.5, pulse_size=600):
    # Both the cut_value and pulse_size should come from the .txt file.
    # Operator must be able to take them into the calculation;
    # Specially because different substrates lead to different variations
    # and the time the pump is working varies with [S];
    """
    Goal:
    Input1: slopes; the product of acc.declive
    Input2:
    Input3:
    Output:
    """

    pH = mat[:, 1]
    pH_antes = pH[: -pulse_size]
    pH_depois = pH[pulse_size:]

    dif = pH_antes - pH_depois

    maxim,_ = scipy.signal.find_peaks(dif, height = cut_value, distance = pulse_size)

    return maxim

def indices_min(mat=slopes, cut_value=1.5, pulse_size=600):
    # Both the cut_value and pulse_size should come from the .txt file.
    # Operator must be able to take them into the calculation;
    # Specially because different substrates lead to different variations
    # and the time the pump is working varies with [S];
    """
    Goal:
    Input1: slopes; the product of acc.declive
    Input2:
    Input3:
    Output:
    """

    pH = mat[:, 1]
    pH_antes = pH[: -pulse_size]
    pH_depois = pH[pulse_size:]

    dif = pH_antes - pH_depois
    dif = -dif

    minim,_ = scipy.signal.find_peaks(dif, height = cut_value, distance = pulse_size)

    return minim


def selecting_entire_pulse(mat, vec = minim):
    # Both the cut_value and pulse_size should come from the .txt file.
    # Operator must be able to take them into the calculation;
    # Specially because different substrates lead to different variations
    # and the time the pump is working varies with [S];
    """
    Goal:
    Input1: slopes; the product of acc.declive
    Input2: output of future_work.indices
    Output:
    """

    '''

    t = []
    pH = []

    for i in np.arange(maxim.shape[0]):
        t1 = mat[maxim[i]:minim[i], 0]
        pH1 = mat[maxim[i]:minim[i], 1]

        t = np.append(t1, t)
        pH = np.append(pH1, pH)

    '''

    max_minus = np.zeros(vec.shape[0]+1)

    for i in np.arange(vec.shape[0]):
        max_minus[i] = vec[i]-1

    max_minus[(vec.shape[0])] = mat.shape[0] # Number of pulses here
    max_minus = max_minus[1:].astype(int)

    t = []
    pH = []

    for i in np.arange(vec.shape[0]):
        t1 = mat[vec[i]:max_minus[i], 0]
        pH1 = mat[vec[i]:max_minus[i], 1]

        t = np.append(t, t1)
        pH = np.append(pH, pH1)


    return t, pH

def breaking_complete_pulse(t, pH):

    all_pulses = []
    pulse = []

    for i in np.arange(pH.shape[0] - 1):
        if pH[i] - pH[600] < -2:
            pulse.append((t[i], pH[i]))

        elif pulse != []:
            AT = np.array(pulse)
            AT[:, 0] = AT[:, 0] - AT[0, 0]
            all_pulses.append(AT)
            pulse = []

    return all_pulses

    pass

maxim = indices_max(slopes)
minim = indices_min(slopes)
t, pH = selecting_entire_pulse(slopes)
plt.plot(t, pH)




mat = acc.read_file('pH412.test', 'Folha4')
clean = acc.cleaning(mat, analise='pH')
slopes = acc.declive(clean, window=100)

t1, pH1 = selecting_entire_pulse(slopes)


all_pulses = acc.breaking(t1, pH1)
#all_pulses = acc.breaking2(all_pulses)
acc.plotting(all_pulses)

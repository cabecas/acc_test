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


def indices(mat, cut_value=1.5, pulse_size=600):
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


def selecting_entire_pulse(mat, maxim):
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

    max_minus = np.array(np.zeros(maxim.shape[0]+1))

    for i in np.arange(maxim.shape[0]):
        max_minus[i] = maxim[i]-1

    max_minus[(maxim.shape[0])] = mat.shape[0] # Number of pulses here
    max_minus = max_minus[1:].astype(int)

    t = []
    pH = []

    for i in np.arange(maxim.shape[0]):
        t1 = mat[maxim[i]:max_minus[i], 0]
        pH1 = mat[maxim[i]:max_minus[i], 1]

        t = np.append(t1, t)
        pH = np.append(pH1, pH)

    return t, pH




'''
mat = acc.read_file('pH412.test', 'Folha4')
clean = acc.cleaning(mat, analise='pH')
slopes = acc.declive(clean, window=100)

t1,pH1 = select_entire_pulse(slopes, maxim)
all_pulses = acc.breaking(t1, pH1)
#all_pulses = acc.breaking2(all_pulses)
acc.plotting(all_pulses)
'''

'''
pH = slopes[:, 1]
pH_antes = pH[:-600]
pH_depois = pH[600:]

dif = pH_antes - pH_depois

plt.plot(dif)
plt.show()
'''

maxim = indices(slopes)
t,pH = selecting_entire_pulse(slopes, maxim)
plt.plot(t, pH)

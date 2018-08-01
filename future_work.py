# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:23:22 2018

@author: ferna
"""

import numpy as np
import acc
import matplotlib.pyplot as plt


def select_entire_pulse(mat, cut_value=1.5, pulse_size=600):

    pH = mat[:, 1]
    pH_antes = pH[: -pulse_size]
    pH_depois = pH[pulse_size:]

    dif= pH_antes - pH_depois

    ixs = np.array(range(len(dif)))

    feed = ixs[dif > cut_value]

    lt = feed[0]
    last = feed[0]

    for ix in feed[1:]:
        if ix > last + 1000:
            pulses_fed = np.append(lt, ix)
            last=ix

    return pulses_fed

'''
mat = acc.read_file('pH412.test', 'Folha4')
clean = acc.cleaning(mat, analise='pH')
slopes = acc.declive(clean, window=100)

t1,pH1 = select_entire_pulse(slopes)
all_pulses = acc.breaking(t1, pH1)
#all_pulses = acc.breaking2(all_pulses)
acc.plotting(all_pulses)
'''

pH = slopes[:, 1]
pH_antes = pH[:-600]
pH_depois = pH[600:]

dif= pH_antes - pH_depois

plt.plot(dif)
plt.show()

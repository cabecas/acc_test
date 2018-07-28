# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:23:22 2018

@author: ferna
"""

import numpy as np
import acc


def select_entire_pulse(mat, set_point1 = 0.2, set_point2 = -3,
                        shift=50):

    #Ver folha do Prof.

    pass


mat = acc.read_file('pH412.test', 'Folha4')
clean = acc.cleaning(mat, analise='pH')
slopes = acc.declive(clean, window=100)

t1,pH1 = select_entire_pulse(slopes)
all_pulses = acc.breaking(t1, pH1)
#all_pulses = acc.breaking2(all_pulses)
acc.plotting(all_pulses)

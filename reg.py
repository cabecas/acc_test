# regressão propriamente dita???

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def pulse_reg(lista):

# Define 1st array of all_pulses as a variable A
    p1 = lista
    #print(p1)                              # Data

# Regression: A*np.exp(-k*x)+C
#Adapt to fun.py

    def func(x, A, k, C):
        return A*C/((C-A)*np.exp(-k*x)+A)

    plt.plot(p1[:,0], p1[:,1], 'b-', label='data')

    popt, pcov = curve_fit(func, p1[:,0], p1[:,1], p0=([7,25,9]))
    plt.plot(p1[:,0], func(p1[:,0], *popt), 'r-',
        label='fit: A=%5.2f, k=%5.4f, C=%5.2f' % tuple(popt))

    #print(popt)                            # Optimization parameters
    #print(np.sqrt(np.diag(pcov)))          # Covariance matrix

    plt.xlabel('t (min)')
    plt.ylabel('pH')
    plt.legend()
    plt.show()

    return popt

#b=pulse_reg(all_pulses[0])

def return_parameter(pulses = all_pulses, parameter = 'k'):

    all_list = [[] for i in range(len(pulses))]
    k_pulse = [None]*3
    n_list = [None]*len(pulses)

    if parameter == 'A':
        a = 0
    elif parameter == 'k':
        a = 1;
    elif parameter == 'C':
        a = 2;
    else:
        print("Please, writing one of the following options: "
              "'A', 'k' or 'C'")

    for i in range(len(pulses)):
        k_pulse = pulse_reg(pulses[i])
        all_list[i] = k_pulse
        n_list[i] = k_pulse[a]

    return n_list

def plot_parameter(parameter_values):



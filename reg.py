import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def pulse_reg(lista):

# Define 1st array of all_pulses as a variable A
    p1 = lista
    print(p1)

# Regression: A*np.exp(-k*x)+C
#Adapt to fun.py

    def func(x, A, k, C):
        return A*C/((C-A)*np.exp(-k*x)+A)

    plt.plot(p1[:,0], p1[:,1], 'b-', label='data')

    popt, pcov = curve_fit(func, p1[:,0], p1[:,1], p0=([7,25,9]))
    plt.plot(p1[:,0], func(p1[:,0], *popt), 'r-',
        label='fit: A=%5.2f, k=%5.4f, C=%5.2f' % tuple(popt))

    print(popt)
    print(np.sqrt(np.diag(pcov)))

    plt.xlabel('t (min)')
    plt.ylabel('pH')
    plt.legend()
    plt.show()

    return popt

b=pulse_reg(all_pulses[1])

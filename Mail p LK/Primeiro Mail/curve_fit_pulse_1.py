import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

file = ('412.xls')
xl = pd.ExcelFile(file)
t= xl.parse('t')
pH= xl.parse('pH')


def func(x, A, k, C):
    return A*C/((C-A)*np.exp(-k*x)+A)
#A*np.exp(-k*x)+C

t = t.iloc[:,0]
t=t.dropna()

pH=pH.iloc[:,0]
pH=pH.dropna()

plt.plot(t, pH, 'b-', label='data')

popt, pcov = curve_fit(func, t, pH, p0=([7,25,9]))
plt.plot(t, func(t, *popt), 'r-',
         label='fit: A=%5.2f, k=%5.4f, C=%5.2f' % tuple(popt))

print(popt)
print(np.sqrt(np.diag(pcov)))

plt.xlabel('t (h)')
plt.ylabel('pH')
plt.legend()
plt.show()
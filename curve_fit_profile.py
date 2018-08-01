'''importing stuff'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


'''Inputs da pessoa'''
fileread = input("Qual é o ficheiro que deve ser lido? \n \n")
decisao = input("Gráfico em função do pulso (p), ou em função do tempo (t)? \n \n")


'''Uploading file; file must have two sheets: one with a matrix of pH values per pulse and another with t;
everything should be normalized, starting with t = 0 h'''
xls=('.xls')
file = fileread + xls
xl = pd.ExcelFile(file)
t = xl.parse('t')
pH = xl.parse('pH')
tpulso = xl.parse('tpulso')


'''dataframe to np.array'''
pH=pH.values
t=t.values
tpulso=tpulso.values


'''tranposing the matrices for easier indexing for me'''
pH=np.transpose(pH)
t=np.transpose(t)


'''defining the function for fitting the values'''
def func(x, A, k, C):
    return A*C/((C-A)*np.exp(-k*x)+A)
#A*np.exp(-k*x)+C


'fitting all 7 sets of values; coeffs variable will store the A, k and C for all fittings'
'Máscara AND/OR?'
coeffs=[]
p0=([7,25,9])
for ix in np.arange(t.shape[0]):
    x=t[ix]
    x = x[~np.isnan(x)]
    y=pH[ix]
    y = y[~np.isnan(y)]
    popt, pcov = curve_fit(func, x, y, p0)
    coeffs.append(popt)
    
    
'''transposing and printing the coefficients'''
coeffs=np.transpose(coeffs)
print(coeffs)


'''plotting k against pulse number'''
if decisao == 'p':
    plt.plot(np.arange(t.shape[0])+1, coeffs[1], 'b-')
    plt.xlabel('pulse')
    plt.ylabel('k')
    plt.xticks(np.arange(1, t.shape[0]+1, 1))
    #plt.legend
    plt.show()


if decisao == 't':
    plt.plot(tpulso[1:tpulso.shape[0]], coeffs[1], 'r-')
    plt.xlabel('tempo')
    plt.ylabel('k')
    #plt.xticks(np.arange(1, t.shape[0]+1, 1))
    #plt.legend
    plt.show()
import numpy as np

def func(t, A, k, C):
    '''
    Parameters A, k and C can be understood;
    k (1/h) is a measure of how quick pH is changing over time;
    lim t->0 = A
    lim t->Inf = C
    '''
    return A*C/((C-A)*np.exp(-k*t)+A)

def func2(x, A, k, C):
    '''
    Parameters A, k and C don't have any biological sense at the moment;
    Good fit though;
    '''
    return A*np.exp(-k*x)+C


#Será que é preciso importar o numpy aqui??
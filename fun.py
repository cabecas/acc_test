import numpy as np

def ode11(t, A, k, C):
    """
    Parameters A, k and C can be understood;
    k (1/h) is a measure of how quick pH is changing over time;
    lim t->0 = A
    lim t->Inf = C
    """

    return A*C/((C-A)*np.exp(-k*t)+A)

def ode12(t, A, k, C):
    """
    Parameters A, k and C have biological sense like ode11;
    Good fit though;
    """

    return A*np.exp(-k*t)+C

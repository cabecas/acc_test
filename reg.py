# regressão propriamente dita???

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import fun as fun

def pulse_reg(p1, func=fun.ode12):

    """

    Goal:
    Input:
    Output:

    """

    plt.plot(p1[:, 0], p1[:, 1], 'b-', label='data')

    popt, pcov = curve_fit(func, p1[:, 0], p1[:, 1], p0=([7, 25, 9]))
    plt.plot(p1[:, 0], func(p1[:, 0], *popt), 'r-',
             label='fit: A=%5.2f, k=%5.4f, C=%5.2f' % tuple(popt))

    #print(popt)                            # Optimization parameters
    #print(np.sqrt(np.diag(pcov)))          # Covariance matrix

    plt.xlabel('t (min)')
    plt.ylabel('pH')
    plt.legend()
    plt.show()

    return popt

#b=pulse_reg(all_pulses[0])


def return_parameter(profile, parameter='k'):

    """

    Goal:
    Input1:
    Input2:
    Output:

    """

    #Checking Input2...
    if parameter == 'A':
        a = 0
    elif parameter == 'k':
        a = 1
    elif parameter == 'C':
        a = 2
    else:
        print("Please, writing one of the following options: "
              "'A', 'k' or 'C'")
        return

    all_list = [[] for i in range(len(profile))]
    k_pulse = [None]*3
    n_list = [None]*len(profile)

    for i in range(len(profile)):
        k_pulse = pulse_reg(profile[i])
        all_list[i] = k_pulse
        n_list[i] = k_pulse[a]

    return n_list


def plot_parameter(parameter_values):

    """
    Neste momento está a funcionar para fazer o gráfico em função do número de pulso. Quando é que alimentou
    efectivamente o pulso para se fazer isto como deve de ser???

    Goal:
    Input:
    Output:

    """

    t_length = len(parameter_values)
    t = range(t_length)
    plt.plot(t, parameter_values, 'b-', label='data')


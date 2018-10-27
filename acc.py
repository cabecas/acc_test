# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:09:37 2018

@author: fernandosilva

Code for the project of DPA as well as dealing with the data from the 
accumulation reactor in the pilot plant;
"""

'''Importing stuff'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_file(fileread, folha):
    """
    Goal: Make data available in Python from the source;
    Input1: Excel file, with type xls;
    Input2: Name of the sheet in the file passed as Input1;
    Output: pandas.df with raw data
    """
            
    xls = ('.xls')
    file = fileread + xls
    xl = pd.ExcelFile(file)
    xl = xl.parse(folha)
    
    return xl


def cleaning(table, analise='pH'):
    '''
    Goal: To wrangle one pandas.df into a simple 2D array, which will be easy to
    handle;
        
    Beware that the file must follow a very strict structure for this to be ok:
        
    - 7 lines with description from Prof. Mário Eusébio's program + 1 empty line
    - 1 line with headers
    - the data to be analysed
        
    Input1: The output of the file_read function; type -> pandas.df;
    Input2: Type of analysis the user wants to carry out. pH is set by default. 
    Later, DO analysis will also be available;
    Output: Function returns a numpy 2D array with the data necessary for the 
    analysis.
    '''
        
    table = table.rename(columns=table.iloc[7])
    table = table.drop(table.index[0:8], axis=0)
    dados = analise+' (Kg)'
    table = table.loc[:, ['Time elapsed (min)', dados]]
    table = table.rename(index=str, columns={"Time elapsed (min)": "time", 
                                           dados: analise})
    table = table.reset_index(drop=True)
    matnp = table.values
    matnp = matnp.astype(float).round(3)
    return matnp

# This function won't be used in this project
def ret_date(table):
    '''
    Goal: This function will support the final report of this analysis by 
    retrieving the date that the experiment took place;
    Input: The output of the file_read function; type -> pandas.df;
    Output: Function returns a string with the date the experiment took
    place.
    '''
    
    date = table.iloc[8][0]
    date = date.isoformat(' ', 'seconds')
    date = date.split(' ')[0]
    
    return date


def linreg(x, y):
    '''
    Goal: This function returns slope and intercept for a simple regression 
    line;
    Input1: takes one 1D numpy array with data to be used as x-data;
    Input2: takes one 1D numpy array with data to be used as y-data;
    Output: slope of the regression (dy/dx).
    '''
    
    # initial sums
    n = float(len(x))
    sum_x = x.sum()
    sum_y = y.sum()
    sum_xy = (x*y).sum()
    sum_xx = (x**2).sum()
    
    # formula for w0
    slope = (sum_xy - (sum_x*sum_y)/n)/(sum_xx - (sum_x*sum_x)/n)
    
    # formula for w1
    # intercept = sum_y/n - slope*(sum_x/n)
    
    return slope


def declive(mat,window=10):
    '''
    Goal: Calculates dy/dx and d2y/dx2 for the vectors x and y, 
    taking into account the number of points given by the user 
    (variable name is window);
    Input1: 2D np.array (m x 2) to be used for the slope calculation, 
    which is the output of the acc.cleaning function; left column is 
    x-data, while right column is y-data; 
    Input2: range of values to taken into account to calculate the slope;
    Output: 2D np.array (m x 4) with the time, parameter and dy/dx and 
    d2y/dx2 values as columns.
    '''
    
    slope = np.zeros((len(mat), 1))
    
    # calculating dy/dx
    for i in range(0, slope.shape[0]-window+1):
        slope_x = linreg(mat[i:window+i,0], mat[i:window+i,1])
        slope[i+window-1] = slope_x
    slope1 = slope.astype(float).round(3)
    
    slope_dydx=np.concatenate((mat, slope1), axis=1)
    
    # calculating d2y/dx2
    for i in range(0, slope.shape[0]-window+1):
        slope_x2 = linreg(slope_dydx[i:window+i,0], slope_dydx[i:window+i,2])
        slope[i+window-1] = slope_x2
    slope2 = slope.astype(float).round(3)
    
    slope_dydx2 = np.concatenate((slope_dydx, slope2), axis=1)

    return slope_dydx2


def selecting(mat, slopes=2, fraction=1/4, 
              target_slope1=0.02, target_slope2=0.001, shift=50):
    '''
    Goal: to select the data relevant for the analysis. Since the most
    important data is the data where the trend ph vs t is increasing (for
    the pH analysis), this is the data that will be selected. And due to
    the rate that the pH increases over time for each pulse decreases 
    (one can say it decelarates??), two slope values will be used to
    select data. note: target_slope1 should ALWAYS be higher than 
    target_slope2;
    Input1: the ouput of declive function; 2D np.array with (m x 4) dimensions;
    Input2: the number of slopes that will be used to select data; it can only
    take the values of 1 or 2;
    Input3: the fraction of values of mat that will be selected based on
    target_slope1;
    Input4: the value of target_slope1;
    Input5: the value of target_slope2;
    Input6: when the slope is calculated, the first window values are all zeros;
    then slopes start being calculated after there's more than window values;
    because of this, the selection of values must taken into account this shift;
    otherwise, values would have a shift of window/2 points to right, which is
    a loss of relevant data;
    Output1: 1D np.array with data of time;
    Output2: 1D np.array with data of pH.
    '''

    if slopes == 1:
        
        t = []
        pH = []
    
        for i in np.arange(0, mat.shape[0]):
            if mat[i, 2] > target_slope1:
                t=np.append(t, mat[i-shift, 0])
                pH=np.append(pH, mat[i-shift, 1])    
            
        return t,pH
    
    if slopes == 2:
        
        n=round(mat.shape[0]*fraction)
        
        t = []
        pH = []
    
        for i in np.arange(0, n):
            if mat[i, 2] > target_slope1:
                t = np.append(t, mat[i-shift, 0])
                pH = np.append(pH, mat[i-shift, 1])
                
        for i in np.arange(n+1, mat.shape[0]):
            if mat[i, 2] > target_slope2:
                t = np.append(t, mat[i-shift, 0])
                pH = np.append(pH, mat[i-shift, 1])
            
        return t, pH


def breaking(t,pH):
    '''
    Goal: After selecting all values of t and pH that are important for the
    analysis, it's important to break the values into a list of numpy arrays 
    so that a plot can later be done. This function does just that!
    Input1: t values obtained from the function selecting;
    Input2: pH values obtained from the function selecting;
    Output: a list of numpy arrays with t and corresponding pH values.
    '''
    
    all_pulses = []
    pulse = []
    
    for i in np.arange(t.shape[0]-1):
        if t[i+1]-t[i] < 1:
            pulse.append( (t[i], pH[i]) )
            
        elif pulse != []:
            AT = np.array(pulse)
            AT[:, 0] = AT[:, 0]-AT[0, 0]
            all_pulses.append(AT)
            pulse = []
    
    return all_pulses


def breaking2(all_pulses, pulsos=5, set_point=1):
    '''
    Goal: Since the function selecting may not work well in the sense that will
    lead to too many sets of values in the breaking function, a second breaking
    function will be used in order to decrease the number of numpy arrays
    to the number of actual pulses of substrate fed to the reactor. The failure
    in the function selecting is not because it is not built correctly, but 
    because the data has a lot of noise and sometimes there is increasing pH
    due to that noise (so, it will appear as if a pulse of substrate was fed to
    the reactor);
    Input1: a list of numpy arrays, which is obtained from the breaking function
    Input2: the number of pulses fed to the reactor on the given day;
    Input3: difference in pH for the maximum and minimum values within a given
    pulse; usually a value of 1 should be more than enough, but on the off chance
    it is not, it has been included as parameter;
    Output: a list of numpy arrays with t and corresponding pH values, as before,
    but now with the length equal to the Input2 (pulsos).
    '''

    a = len(all_pulses)
    j = 0
    
    while j != pulsos:
        try:
            for i in np.arange(a):
                maxi = max(all_pulses[i][:, 1])
                mini = min(all_pulses[i][:, 1])
            
                if maxi - mini < set_point:
                    del(all_pulses[i])
                    a = len(all_pulses)
                    
        except IndexError:
            pass
        j = len(all_pulses)
        print(j)    
        
    return all_pulses
            

def plotting(data):
    '''
    Goal: To plot the result of the function breaking2;
    Input: The result of the function breaking2;
    Output: A plot;
    '''

    n = len(data)
    fig, ax = plt.subplots(figsize=(12, 6)) #create figure and axes
    for i in np.arange(n):
    #now plot data set i
        ax.plot(data[i][:, 0], data[i][:, 1])
        plt.plot()
        plt.legend(np.arange(n)+1)
        ax.set_xlabel('time (min)', color='w', fontsize=12)
        ax.set_ylabel('pH', color='w', fontsize=12)
        ax.tick_params(axis='y', labelcolor='w', labelsize=14)
        ax.tick_params(axis='x', labelcolor='w', labelsize=14)
        


#testing declive - Resultado Final
        
mat = read_file('pH412.test', 'Folha4')
clean = cleaning(mat, analise='pH')
slopes = declive(clean, window=100)
t,pH = selecting(slopes, slopes=2, fraction=1/4,
              target_slope1=0.02, target_slope2=0.001, shift=50)
all_pulses = breaking(t, pH)
all_pulses = breaking2(all_pulses, pulsos=5, set_point=1)
plotting(all_pulses)
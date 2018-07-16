# -*- coding: utf-8 -*-
"""
Test code for the file acc;
User should copy these lines, paste then in the acc.py file and run it to test it!
"""
       
### READ_FILE-------------------------------------------------------------------
    
print(read_file('pH412.test','Folha1'))
help('read_file')
    

### CLEANING-------------------------------------------------------------------
    
print(cleaning(read_file('pH412.test','Folha1')))
print(cleaning(read_file('pH412.test','Folha1')).shape)
print(cleaning(read_file('pH412.test','Folha1'),'DO'))
print(type((cleaning(read_file('pH412.test','Folha1')))))
help('cleaning')
    

### RET_DATE-----------------------------------------------------------------
    
print(ret_date(read_file('pH412.test','Folha1')))
print(type(ret_date(read_file('pH412.test','Folha1'))))
help('ret_date')
    

### LINREG---------------------------------------------------
    
x=np.array([1,2,3,4])
y=np.array([1,2,3,4])
print(linreg(x,y))    


### DECLIVE--------------------------------------------------------------------
xval=np.array([1,2,3,4,5,6,7,8,9,10])[:,None]
yval=np.array([4,5,6,5,4,3,2,1,2,3])[:,None]
xy=np.concatenate((xval,yval),axis=1)
test=declive(xy, 2)
fig, ax1 = plt.subplots(figsize=(10,6))
plt.plot(test[:,0],test[:,1])
ax1.tick_params(axis='y', labelcolor='w', labelsize=14)
ax1.tick_params(axis='x', labelcolor='w', labelsize=14)
print(test[0:9])



matnp=cleaning(read_file('pH412.test','Folha4'))
slope_array=declive(matnp)
print(slope_array[0:6,:])

slope_array[:,2]=slope_array[:,2]*10
slope_array[:,3]=slope_array[:,3]*10

fig, ax1 = plt.subplots(figsize=(10,6))

color = 'tab:red'
ax1.set_xlabel('time (min)', color='w', fontsize=12)
ax1.set_ylabel('pH', color='w', fontsize=12)
ax1.plot(slope_array[:,0],slope_array[:,1], color=color)
ax1.tick_params(axis='y', labelcolor='w', labelsize=14)
ax1.tick_params(axis='x', labelcolor='w', labelsize=14)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('slope', color='w', fontsize=12)  # we already handled the x-label with ax1
ax2.plot(slope_array[:,0],slope_array[:,2], color=color)
ax2.tick_params(axis='y', labelcolor='w', labelsize=14)

color = 'tab:green'
ax2.plot(slope_array[:,0],slope_array[:,3], color=color)

plt.legend(['pH','dydx','d2ydx2'])
plt.xlim([100,400])

plt.show()


### SELECTING--------------------------------------------------------------

mat=read_file('pH412.test','Folha4')
mat=cleaning(mat,analise='pH')
mat=declive(mat)
t,pH=selecting(mat)
print(t)
print(pH)

#plots_test
fig, ax1 = plt.subplots(figsize=(10,6))

#plot_slope_pH-vs-t
color = 'darkblue'
ax1.set_ylabel('slope', color='w', fontsize=12)  # we already handled the x-label with ax1
ax1.plot(mat[:,0],mat[:,2], color=color, linewidth=2)
ax1.tick_params(axis='y', labelcolor='w', labelsize=14)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

#plot_pH_pre-breaking
color = 'darkred'
ax2.set_xlabel('time (min)', color='w', fontsize=12)
ax2.set_ylabel('pH', color='w', fontsize=12)
ax2.plot(mat[:,0],mat[:,1], color=color, linewidth=2)
ax2.tick_params(axis='y', labelcolor='w', labelsize=14)
ax2.tick_params(axis='x', labelcolor='w', labelsize=14)

#plot_pH_pos-breaking
color = 'limegreen'
ax2.plot(t,pH, 'go', linewidth=3, ms=3)
ax2.tick_params(axis='y', labelcolor='w', labelsize=14)

plt.show()


### BREAKING & BREAKING2------------------------------------------------------
    
#testing declive
mat=read_file('pH412.test','Folha4')
slopes=declive(cleaning(mat))

#selecting relevant data
t,pH=selecting(slopes)
all_pulses=breaking(t,pH)
all_pulses=breaking2(all_pulses)


fig, ax1 = plt.subplots(figsize=(10,6))

color = 'tab:blue'
ax1.set_xlabel('time (min)', color='w', fontsize=12)
ax1.set_ylabel('slope', color='w', fontsize=12)
ax1.plot(slopes[:,0],slopes[:,2], color=color)
ax1.tick_params(axis='y', labelcolor='w', labelsize=14)
ax1.tick_params(axis='x', labelcolor='w', labelsize=14)
plt.ylim((0,10))

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('pH', color='w', fontsize=12)  # we already handled the x-label with ax1
ax2.plot(slopes[:,0],slopes[:,1], color=color)
ax2.tick_params(axis='y', labelcolor='w', labelsize=14)

color = 'limegreen'
ax2.plot(t,pH, 'go', linewidth=3, ms=3)
ax2.tick_params(axis='y', labelcolor='w', labelsize=14)
plt.show()

#print(all_pulses)
print(len(all_pulses))


### Random stuff---------------------------------
    
for i in range(0,5):
    print(i)
    
import numpy as np
N = 10
a = np.random.rand(N,N)
b = np.zeros((N,N+1))
b[:,:-1] = a
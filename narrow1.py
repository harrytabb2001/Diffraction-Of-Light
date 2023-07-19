#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:15:50 2021

@author: harrytabb
"""

import numpy as np
import matplotlib.pyplot as plt

#Creating figure and axis
fig, ax = plt.subplots()

#Importing data
data = np.genfromtxt('narrow1.txt', dtype=float, delimiter=',')

#Seperating data into collumns
time_array = np.array(data[:,0])
distance_array = time_array * 0.00015
voltage_array = np.array(data[:,1])

#Plotting Data
ax.minorticks_on()
plt.grid(which='both', linewidth = 0.5)
plt.plot(distance_array, voltage_array, 'r')
plt.xlabel("Distance (m)")
plt.ylabel("Voltage (m)")
plt.title("Narrow Run 1")
plt.axvline(0.0293,0,1)
plt.axvline(0.0233,0,1)
plt.axhline(0.318,0,1)
plt.plot()
plt.savefig('NarrowRun1.png', dpi = 1000)


x_max = 0.0293
x_min = 0.0233
difference_in_x1 = x_max -x_min
print('{:.5f}'.format(difference_in_x1))

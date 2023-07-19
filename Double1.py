#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:44:39 2021

@author: harrytabb
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

data = np.genfromtxt('double1.txt', dtype=float, delimiter=',')

time_array = np.array(data[:,0])
distance_array = time_array * 0.00015
distancezero = (distance_array - 0.0141) * 10**3
ratio = distancezero/0.16
theta = np.arctan(ratio)

a = np.linspace(-0.05,0.05)
phid = np.pi / (670*10**(-9)) *0.000214 * np.sin(a)
phia = np.pi / (670*10**(-9)) *0.00005 * np.sin(a)
I = (np.cos(phid))**(2) * (np.sin(phia)/(phia))**2
#plt.axvline(0.0141)
#plt.axvline(0.0146)
#plt.plot(a, I) 


voltage_array = np.array(data[:,1])
ax.minorticks_on()
plt.grid(which='both', linewidth = 0.5)
plt.plot(distancezero, voltage_array, 'r')
plt.xlabel("Theta")
plt.ylabel("Voltage (V)")
plt.title("Double Run 1 Sinc")
plt.axvline(0)
plt.axvline(1.52)
plt.xticks(np.arange(-4,5, 1))

#plt.savefig('DoubleRun1Sinc.png', dpi = 1000)



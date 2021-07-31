# -*- coding: utf-8 -*-
"""                     generating basic signals
                    Created on Wed Jul 28 17:56:20 2021

                          @author: Mosharof
"""
#%% importing library
import matplotlib.pyplot as plt
import numpy as np

#%% closing all previous plot
plt.close("all")

#%% number of sample
n = np.arange(-10, 10)
# length of n
l = np.size(n)

#%% generating impulse signal
imp = np.zeros(l)
ind = np.where(n == 0)
imp[ind] = 1

#%% plotting impulse signal
plt.stem(n,imp); plt.title("impulse signal")
plt.xlabel("sample number"); plt.ylabel("amplitude")

#%% generating unit step unit step signal
us = np.zeros(l)
ind = np.where(n >= 0)
us[ind] = 1

#%% plotting unit step
plt.figure(2)
plt.stem(n,us); plt.title("unit step")
plt.xlabel("number of sample"); plt.ylabel("Amplitude")

#%% generating ramp signal
rs = np.zeros(l)
ind = np.where(n >= 0)
rs[ind] = n[ind]

#%% plotting ramp signal
plt.figure(3)
plt.stem(n,rs);plt.title("ramp signal")
plt.xlabel("sample number");plt.ylabel("amplitude")

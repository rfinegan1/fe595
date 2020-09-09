#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:21:15 2020

@author: ryanfinegan
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,.01)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()
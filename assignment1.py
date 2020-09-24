#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:21:15 2020

@author: ryanfinegan
"""

#importing libraries needed for the first assignment 
import numpy as np
import matplotlib.pyplot as plt

def main():
    #assignment said for one period which is 2 pi 
    period = np.arange(0,2*np.pi,.01)
    x = np.sin(period)
    y = np.cos(period)
    z = np.tan(period)
    plt.plot(period,x,period,y,period,z)
    # Adding ylim prevents the graph from being skewed as tangent values go to infinity
    plt.ylim(-4, 4)
    plt.show()
    
if __name__ == '__main__':
    main()

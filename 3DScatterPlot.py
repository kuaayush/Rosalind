# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:01:15 2021

@author: Administrator
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
xlist = [1, 2, 3, 4, 5]
ylist = [1, 5, 3, 4, 2]
zlist = [6, -3, 6, -1, 2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xlist, ylist, zlist)
plt.ticklabel_format(useOffset=False)   
plt.show()
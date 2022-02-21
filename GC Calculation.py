# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:52:51 2020

@author: Administrator
"""

keywords ='>'
gc = open ("rosalind_gc.txt", "r")

# #print(gc.read())

# read by character 
# 	
# while 1: 
#    char = gc.read(1014)
#    if not char:
#         break
#    print(char) 
line=gc.readline()
if keywords in gc:
    for line in range(len(line)):

        d = gc.readline()
    tot = len(d)
    a = d.count("A")
    t = d.count("T")
    g = d.count("G")
    c = d.count("C")

    s = ((g + c)/tot)*100
    print(s, "%")

# tm = (4*(g+c)) + (2*(a+t))
# print("The melting temperature of given sequence is:", tm, "degree Celcius")
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:20:29 2021

@author: Administrator
"""


def MendelFirstLaw(k,m,n): #The idea to use a user defined function derived from Sandesh Dai 
    
    t =  k + m + n 
    kk = k/t * (k-1)/(t-1) #k is homozygous for dominant, thus probability is 1
    km = k/t * m/(t-1)
    kn = k/t * n/(t-1)
    
    mk = m/t * k/(t-1) # cross of homozygous dominant and heterozygous gives dominant offspring
    mm = 3/4 * m/t * (m-1)/(t-1) # cross between two heterozygous: dominant offspring ratio is 3:4
    mn = (1/2) * (m/t)* n/(t-1) # cross between heterozygous and homozygous recessive; dominant offspring ratio is 1:2
    
    nk = n/t * k/(t-1) # k is homozygous dominant
    nm = (1/2) * (n/t) * m/(t-1) # cross between heterozygous and homozygous recessive; dominant offspring ratio is 1:2
    nn = n/t * (n-1)/(t-1) # all homozygous recessives
    
    prob = kk + km + kn + mk + mm + mn + nk + nm 
    print(prob)

k, m, n = 15, 24, 22 
MendelFirstLaw(k, m, n)
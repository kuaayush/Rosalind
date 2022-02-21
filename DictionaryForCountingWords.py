# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:48:27 2021

@author: Administrator
"""


string = input("Enter the text:")
text = string.split(" ")
print('\n')
dic = {}

for word in text:
    dic[word] = text.count(word)

for word, count in dic.items():
    print (word, count)


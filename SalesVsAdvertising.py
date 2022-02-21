# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:22:05 2021

@author: Administrator
"""


import pandas as pd
import numpy as np

species_label = dict()
iris_data = pd.read_csv('iris.csv')
species = iris_data['Species']
for i in species:
    if i == 'Iris-setosa':
        species_label['serosa'] = 0
    if i == 'Iris-versicolor':
        species_label['versicolor'] = 1
    if i == 'Iris-virginica':
        species_label['virginica'] = 2
print(species_label)
print(type(species_label))


# target = pd.DataFrame(species_label)
#iris_data['Species'].value_counts().plot(kind='bar', width = 0.2)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_file = pd.read_csv('sales.csv')

ad = list(sales_file['Advertising'])
sale = list(sales_file['Sales'])

print(ad, '\n', sale)


plt.subplot(1,2,1)
plt.scatter(sale, ad)
plt.xlabel("Sales")
plt.ylabel("Advertising")
plt.title("Effect of advertising")

plt.subplot(1,2,2)
plt.hist(sale,color ='red')
plt.title("Repitition of Sales")
plt.xlabel("Sales")


plt.show()











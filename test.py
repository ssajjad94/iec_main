# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:20:14 2020

@author: sajjad
"""

from printbar import printbar

# tuples - immutable

t1 = ()
t2 = (1, 2, 3, 'str', 9, 8, 10)
t3 = (3, 2 ,1, 'strrr, strr,', 'strr', 11)

l = [2, 2, 3, 4 , 5, 'h', 6, "red"]

# list - indexed

even = []
odd = []
for year in range (2020, 2040):
    if (year%2 == 0):
        even.append(year)
    else:
        odd.append(year)
        

printbar()
print(f"even years: {even}")
printbar()
print(f"odd years: {odd}")
        

# dictionaries = key-value pair

d1 = {'name':'sajjad', 'class': 'python'}

d1['age'] = '26'
d1['age'] = '25'

d2 = {"name": "sajjad",
      "class": ["python", "DevOps"],
      "location": "Chicago"}

print (d1)

printbar()
for key, value in d2.items():
    print(key, value, sep=':')    
printbar()
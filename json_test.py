#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:46:26 2020
example of json and python dict
@author: sajjad
"""
import printbar as pb



my_dict = {'grades': [
         {'id': 100, 'name': 'John 1', 'grade': 98},
         {'id': 102, 'name': 'John 2', 'grade': 88},
         {'id': 103, 'name': 'John 3', 'grade': 58},
         {'id': 104, 'name': 'John 4', 'grade': 78},
         {'id': 105, 'name': 'John 5', 'grade': 48},
         {'id': 106, 'name': 'John 6', 'grade': 68},
]}

print(my_dict)
pb.printbar()

import json

try:    
    with open('grades2.json', 'w') as grades:
        json.dump(my_dict, grades)
except:
    print("error")
else:
    print("else")
finally:
    print("finally here")
        
pb.printbar()   
## read the json file
with open('grades2.json', 'r') as grades:
    my_grades = json.load(grades)

print(my_grades)
pb.printbar()

# 
print(json.dumps(my_grades,indent=2))
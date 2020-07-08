#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:49:06 2020

@author: fali

install requests module
conda env list
conda activate fa-test
conda install 
conda install  --help
conda install  requests

# we will be using the following for api calls
https://www.frankfurter.app/docs/
https://api.github.com
"""
import printbar as pb
import requests
from requests.exceptions import HTTPError
import json

# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)

#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
        
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
    
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
    
#     else:
#         print(f'Access to {url}: Success!')
        
# pb.printbar()

# # print(json.dumps(response.json(),indent=3))

# url = "https://api.github.com/user"

# auth = ('s.sajjad.94@gmail.com', '191smshhr')

# rs = requests.get(url, auth=auth)
# print(rs.status_code)

# # look at the content
# print(rs.content)
# pb.printbar()

# print(json.dumps(rs.json(),indent=4))

# pb.printbar()

url = "https://api.frankfurter.app/latest"

# rs1 = requests.get(url)

# print(json.dumps(rs1.json(),indent=3))

# params= {'from':'USD'}

# rs2 = requests.get(url, params=params)

# print(json.dumps(rs2.json(),indent=3))

params= {'from':'USD', 'to':'CAD'}

rs3 = requests.get(url, params=params)
# print(json.dumps(rs3.json(),indent=3))


params= {'amount':100,'from':'USD', 'to':'CAD'}
rs4 = requests.get(url, params=params)

today = rs4.json()

print(f"For today:{today['date']}, \
{today['amount']} {today['base']} will get us {today['rates']['CAD']} CAD")

# print(json.dumps(rs4.json(),indent=2))

# payload = {'key1': 'value1'}
# rs = requests.post("url/post", data=payload )
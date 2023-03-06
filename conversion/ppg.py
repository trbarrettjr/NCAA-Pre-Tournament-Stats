#!/usr/bin/python3
import json

# The object from here is to convert the tabular data to json data for processing

f = open('ppg.txt')
data = f.readlines()
for i, v in enumerate(data):
    data[i] = v.strip()

for i, v in enumerate(data):
    data[i] = v.split('\t')

f.close()

keys = data[0].copy()
values = data[1:].copy()

mylist = list()

for item in values:
    mylist.append({k:v for k,v in zip(keys,item)})

w = open('ppg.json', 'w')
my_out = json.dumps(mylist)
w.write(my_out)
w.close()
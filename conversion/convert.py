#!/usr/bin/python3
import json
import sys

# The object from here is to convert the tabular data to json data for processing

if len(sys.argv) == 2:
    fn = sys.argv[1]
else:
    print('Missing Filename: {} [filename]'.format(sys.argv[0]))
    exit()

f = open(fn)
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

outname = fn.split('.')[0] + ".json"

w = open(outname, 'w')
my_out = json.dumps(mylist)
w.write(my_out)
w.close()
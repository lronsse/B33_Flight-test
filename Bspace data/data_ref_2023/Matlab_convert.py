import pandas as pd
import mat4py as mp


annots = mp.loadmat('data.mat')
#print(annots['flightdata'].keys())
keys = []
with open('Dspace Parameters.txt', 'r') as t:
    for i in t:
        i = i.strip('\n')
        keys.append(i)
print(annots['flightdata']['vane_AOA']['data'])

'''
data_list = []
units_list = []
description_list = []

for i in keys:
    try:
        data_list.append(annots['flightdata'][i]['data'])
        description_list.append(annots['flightdata'][i]['description'])
        units_list.append(annots['flightdata'][i]['units'])
    except:
        print(f'broke at i = {i}')
        pass'''

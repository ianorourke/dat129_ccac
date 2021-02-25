# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:59:04 2021

@author: Sale
"""


import json

desk_objects = {}

desk_objects['Pens'] = 9
desk_objects['Pencils'] = 2
desk_objects['Air Duster'] = 'Canister'
desk_objects['Scribbler'] = 'Notebook'
desk_objects['Nearby Paints'] = ['Red','Yellow','Blue','White','Black','Brown']


print(json.dumps(desk_objects))

with open('desk_objects.json','w') as desk_inv:
    desk_inv.write(json.dumps(desk_objects))
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:37:48 2021

@author: RohanLaptop
"""
import numpy as np
import math
from itertools import permutations
data_left = np.load(r"C:\Users\Rohan's Laptop\Downloads\ttbar-lep-left\ttbar-lep-left\event_record_top_lep_left_2.npz")
data_right = np.load(r"C:\Users\Rohan's Laptop\Downloads\ttbar-lep-right\ttbar-lep-right\event_record_top_lep_right_2.npz")
permutations_left = []
for i in range(0, len(data_left['jet_num_of_jets'])):
    permutations_left.append(math.factorial(data_left['jet_num_of_jets'][i])/(math.factorial(list(data_left['jet_btag'][i]).count(1)) * math.factorial((data_left['jet_num_of_jets'][i] - list(data_left['jet_btag'][i]).count(1) ))))
#print(permutations_left)
permutations_right_calc = []
for i in range(0, len(data_right['jet_num_of_jets'])):
    permutations_right_calc.append(int(math.factorial(data_right['jet_num_of_jets'][i])/(math.factorial(list(data_right['jet_btag'][i]).count(1)) * math.factorial((data_right['jet_num_of_jets'][i] - list(data_right['jet_btag'][i]).count(1) )))))
#print(permutations_right)
full_permutations_right = []
permutations_iter = []
for i in range(0, len(data_right['jet_num_of_jets'])):
    permutes = []
    full_permutes=set()
    for j in range(0, (list(data_right['jet_btag'][i]).count(1))):
        permutes.append('b')
    for k in range(0, ((data_right['jet_num_of_jets'][i] - list(data_right['jet_btag'][i]).count(1) ))):
        permutes.append('q')
    #print('permutes: ', permutes)
    permutes = permutations(permutes)
    for l in permutes:
        full_permutes.add((l))
    full_permutes = list(full_permutes)
    permutations_iter.append(len(full_permutes))
   # print('full permutes:',len(full_permutes))
    full_permutations_right.append(full_permutes)
print(full_permutations_right)
errors_num = 0
for i in range(0, len(permutations_right_calc)):
    if permutations_right_calc[i] != permutations_iter[i]:
        errors_num += 1
    else:
        continue
print(errors_num)

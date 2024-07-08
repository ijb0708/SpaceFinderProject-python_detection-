'''
Created on 2020. 7. 25.

@author: Administrator
'''
from _operator import itemgetter

import numpy as np

a= np.array([[[100,3], [2,5], [2,5], [2,5]]])

p = []

p.append(a)
a= np.array([[[1000,3], [2,5], [2,5], [2,5]]])
p.append(a)
a= np.array([[[10,3], [2,5], [2,5], [2,5]]])
p.append(a)
a= np.array([[[1,3], [2,5], [2,5], [2,5]]])
p.append(a)

print(p)

for idx, t in enumerate(p) :
    
    for j in range(idx+1, len(p)):
#         print("t")
#         print(p[idx][0][0][0]," te ", p[j][0][0][0])
        if (p[idx][0][0][0]>p[j][0][0][0]) :
#             print(t[0][idx][0]," te ", t[0][j][0])
            temp = p[idx]
            p[idx] = p[j]
            p[j] = temp

print(p)




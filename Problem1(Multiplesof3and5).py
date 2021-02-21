# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:32:55 2020

@author: Umut Atakul
"""
# Problem 1 (Multiples of 3 and 5)

import numpy as np

listall= np.arange(1,1000) # 1000'e kadar tüm sayıların listesi 
                           # 1000 hariç!

x = [] #3 ve 5 e bölünebilen sayılıarı eklemek için boş liste
for a in listall :
    if  a%3==0 or a%5==0:
        x.append(a)
        
toplam= sum (x) 



print (toplam)

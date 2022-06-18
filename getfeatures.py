# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:10:25 2016

@author: 16727_000
"""
import pandas as pd
from sklearn.feature_extraction.text import HashingVectorizer
mescon_all = pd.read_csv('result.csv',header=None,encoding='utf8')
listtodel = []
for i,line in enumerate(mescon_all[1]):
    if type(line)!=str:
        listtodel.append(i)
mescon_all = mescon_all.drop(listtodel)   #去除无效短信

#vector=TfidfVectorizer(CountVectorizer())
#temp = vector.fit_transform(mescon_all[1]).todense()
outfile = open('features.txt','wb+')

vector = HashingVectorizer(n_features=100)
temp = vector.transform(mescon_all[1]).todense()
x = [[i,j] for i,j in enumerate(mescon_all[0])]
temp = temp.tolist()
print(temp)
for i,line in enumerate(temp):
    outstr = ''
    for word in line:
        outstr += str(word+1)
        outstr += ' ' 
    outfile.write((str(mescon_all[0][x[i][1]])+','+outstr).encode('utf-8')+b'\n')
    
outfile.close()
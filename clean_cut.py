# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:36:39 2016

@author: 16727_000
"""


import pandas as pd
import jieba
import re

mescon_all = pd.read_csv('whole.csv',header=None,encoding='utf8')
#print(mescon_all)
outfile = open('result.csv','wb+')
ns = 0
ps = 0
for i in range(len(mescon_all)):
    mescon_single = mescon_all[2][i]
    me_cate = mescon_all[1][i]
    outstr = ''
    temp = re.sub(u'[^\u4e00-\u9fa5A-Za-z]','',mescon_single)
    ms_cut = list(jieba.cut(temp,cut_all=False))
    for word in ms_cut:
        if word != ' ':
            outstr += word+' '

    if me_cate == 1:
        ns = ns+1
        if ns <80000:
            outfile.write((str(me_cate)+','+outstr).encode('utf-8')+b"\n")
    if me_cate == 0:
        ps = ps+1
        if ps <80000:
            outfile.write((str(me_cate)+','+outstr).encode('utf-8')+b"\n")

outfile.close()


    
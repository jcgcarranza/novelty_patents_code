# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:11:19 2017

@author: Juan Carlos Gomez
@email: jc.gomez@ugto.mx
"""

main_dir = 'C:/Users/JC/Documents/CodeandData/datasets/2017_novelty_patents/'

bow_file = main_dir+'patent_bow.txt'
voca_file = main_dir+'vocabulary.txt'

voca = {}
i = 0
with open(bow_file,'r') as bow_reader:
    for line in bow_reader:
        tokens = line.rstrip().split()
        patent_id = tokens[0]
        voca_doc = {}
        for token in tokens:
            voca_doc[token] = 1
        for token in voca_doc:
            voca[token] = voca.get(token,0)+1
        i += 1
        if i%100000 == 0:
            print('processed ',i,' lines')

keys = [*voca]
for key in keys:
    if voca[key] < 2:
        del voca[key]

with open(voca_file,'w') as voca_writer:
    for key,val in voca.items():
        voca_writer.write(key+'\n')
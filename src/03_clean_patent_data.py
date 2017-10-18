# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:11:19 2017

@author: Juan Carlos Gomez
@email: jc.gomez@ugto.mx
"""

main_dir = 'C:/Users/JC/Documents/CodeandData/datasets/2017_novelty_patents/'

bow_file = main_dir+'patent_bow.txt'
words_file = main_dir+'patent_words.txt'
voca_file = main_dir+'vocabulary.txt'

voca = {}
with open(voca_file,'r') as voca_reader:
    for line in voca_reader:
        voca[line.rstrip()] = 1

i = 0
with open(words_file,'w') as words_writer:
    with open(bow_file,'r') as bow_reader:
        for line in bow_reader:
            tokens = line.rstrip().split()
            patent_id = tokens[0]
            text = ' '.join([token for token in tokens[1:] if token in voca])
            words_writer.write(patent_id+' '+text+'\n')
            i += 1
            if i%50000 == 0:
                print('processed ',i,' lines')
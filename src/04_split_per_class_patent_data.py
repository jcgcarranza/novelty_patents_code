# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:11:19 2017

@author: JC
"""

main_dir = 'C:/Users/JC/Documents/CodeandData/datasets/2017_new_paper_sam/'

words_file = main_dir+'patent_words.txt'
class_file = main_dir+'patent_classes.txt'

classes = {}
with open(class_file,'r') as class_reader:
    for line in class_reader:
        tokens = line.rstrip().split()
        classes[tokens[0]] = tokens[1]

data = {}
i = 0
with open(words_file,'r') as words_reader:
    for line in words_reader:
        tokens = line.split()
        patent_id = tokens[0]
        classe = classes.get(patent_id)
        data[classe] = data.get(classe,[])
        data[classe].append(line)
        i += 1
        if i%50000 == 0:
            print('processed ',i,' lines')

for classe,lines in data.items():
    class_file = main_dir+'class_'+classe+'.txt'
    with open(class_file,'w') as class_writer:
        for line in lines:
            class_writer.write(line)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:11:19 2017

@author: JC
"""

main_dir = 'C:/Users/JC/Documents/CodeandData/datasets/2017_new_paper_sam/'

focal_file = main_dir+'award_control_sample_grouped.txt'
sorted_file = main_dir+'award_control_sorted.txt'

data = {}
with open(focal_file,'r') as focal_writer:
    focal_writer.readline()
    for line in focal_writer:
        columns = line.rstrip().split(',')
        patent_id = columns[0]
        classe = columns[1]
        data[classe] = data.get(classe,[])
        data[classe].append(patent_id)

with open(sorted_file,'w') as sorted_writer:
    for classe,patent_ids in data.items():
        for patent_id in patent_ids:
            sorted_writer.write(classe+' '+patent_id+'\n')
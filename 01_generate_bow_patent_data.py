# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 18:04:45 2017

@author: JC
"""

import re
from nltk.corpus import stopwords

main_dir = 'C:/Users/JC/Documents/CodeandData/datasets/2017_new_paper_sam/'

patent_file = main_dir+'patent_data_no_family.txt'
bow_file = main_dir+'patent_bow.txt'
patent_adates = main_dir+'patent_adates.txt'
patent_classes = main_dir+'patent_classes.txt'

cachedStopWords = stopwords.words('english')

pattern = '[a-z0-9][a-z0-9\-]*'
pattern2 = '[0-9\-]+'
i = 0
with open(bow_file,'w') as bow_writer, open(patent_adates,'w') as adates_writer, open(patent_classes,'w') as classes_writer:
    with open(patent_file,'r') as patent_reader:
        patent_reader.readline()
        for line in patent_reader:
            line = line.rstrip().lower()
            columns = line.split(',')
            patent_id = columns[0]
            patent_class= columns[2]
            patent_adate = columns[3]+' '+columns[4]
            tokens = re.findall(pattern,columns[1])
            tokens.sort()
            text = ' '.join([token for token in tokens if token not in cachedStopWords and len(token)>1 and not re.match(pattern2,token)])
            bow_writer.write(patent_id+' '+text+'\n')
            classes_writer.write(patent_id+' '+patent_class+'\n')
            adates_writer.write(patent_id+' '+patent_adate+'\n')
            i += 1
            if i%50000 == 0:
                print('Processes ',i,' lines...')
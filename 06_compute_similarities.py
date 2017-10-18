# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:11:19 2017

@author: JC
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def read_focal_patents(file):
    focal_patents = {}
    with open(file,'r') as reader:
        for line in reader:
            columns = line.rstrip().split()
            classe = columns[0]
            patent_id = columns[1]
            focal_patents[classe] = focal_patents.get(classe,[])
            focal_patents[classe].append(patent_id)
    return focal_patents

def read_adates_file(file):
    adates = {}
    with open(file,'r') as reader:
        for line in reader:
            columns = line.rstrip().split()
            patent_id = columns[0]
            adate = columns[1]
            adates[patent_id] = adate
    return adates

def read_class_data(file):
    data = {}
    with open(file,'r') as reader:
        for line in reader:
            columns = line.rstrip().split()
            patent_id = columns[0]
            text = ' '.join([token for token in columns[1:]])
            data[patent_id] = text
    return data

def collect_data_past(adate_focus, data, adates):
    sample = []
    for patent_id in data:
        if int(adates.get(patent_id)) < adate_focus:
            sample.append(data.get(patent_id))
    return sample

def collect_data_future(adate_focus, data, adates):
    sample = []
    for patent_id in data:
        if int(adates.get(patent_id)) > adate_focus:
            sample.append(data.get(patent_id))
    return sample

main_dir = 'C:/Users/JC/Documents/CodeandData/datasets/2017_new_paper_sam/'
class_dir = main_dir+'class_files/'

sorted_file = main_dir+'award_control_sorted.txt'
adates_file = main_dir+'patent_adates.txt'

print('Reading focal patents indexes...')
focal_patents = read_focal_patents(sorted_file)
print('Reading adates from patents...')
adates_patents = read_adates_file(adates_file)

dist = {}
#i = 0
j = 0
print('Computing distances...')
for classe,focal_ids in focal_patents.items():
    print('\t Class = ',classe)
    class_file = class_dir+'class_'+classe+'.txt'
    patent_class_data = read_class_data(class_file)
    for focus_id in focal_ids:
        adate = int(adates_patents.get(focus_id))
        focus_patent = patent_class_data.get(focus_id)
        
        sample_past = collect_data_past(adate, patent_class_data, adates_patents)
        sample_past.append(focus_patent)
        vec_past = TfidfVectorizer(norm='l2')
        fit_past = vec_past.fit_transform(sample_past)
        focus_past = fit_past[-1]
        fit_past = fit_past[:-1]
        #focus_past = vec_past.transform([focus_patent])
        sim_past = cosine_similarity(focus_past,fit_past)
        sim_past = np.mean(sim_past[0])
        
        sample_future = collect_data_future(adate, patent_class_data, adates_patents)        
        sample_future.append(focus_patent)
        vec_future = TfidfVectorizer(norm='l2')
        fit_future =vec_future.fit_transform(sample_future)
        focus_future = fit_future[-1]
        fit_future = fit_future[:-1]
        #focus_future = vec_future.transform([focus_patent])
        sim_future = cosine_similarity(focus_future,fit_future)
        sim_future = np.mean(sim_future[0])
        
        dist[focus_id] = [sim_past, sim_future]
        j += 1
        print('\t\t',j)

distances_file = main_dir+'cosine_similarities_award_control_v3.txt'        
with open(distances_file, 'w') as distances_writer:
    for focus_id,distances in dist.items():
        distances_writer.write('%s %.5f %.5f\n' % (focus_id,distances[0],distances[1]))
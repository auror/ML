from __future__ import division
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB

MLNB = []

ftd = open('td.txt','r')
lines = ftd.readlines()
ftd.close()
features = []
Labels = []
Data = []
Synopsis = []
Dic = []

Lab = ['unknown','Action','Adventure','Animation',"Children's","Comedy",'Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']

for i in Lab:
    MLNB.append(GaussianNB())
    
Genres = []

for line in lines:
    temp = line.split(' ')
    Labels.append(temp[-19:])

    temp = temp[:-19]
    temp = [int(x) for x in temp]
    features.append(temp)

L = len(features)
"""for i in range(0, len(features)):
    print features[i]
    #features[i] = [int(x) for x in features[i]]
    Data.append(features[i])"""
Data = features

for j in range(0,19):
    y = []
    for i in Labels:
        if i[j]=='0' or i[j]=='0\n':
            y.append(0)
        else:
            y.append(1)
    Genres.append(y)

for i in range(0,19):
    MLNB[i].fit(Data,Genres[i])


fp = open('data1.txt','r')

lines = fp.read()
fp.close()

words = lines.split(' ')


syn = open('Synopsis.txt','r')
f = syn.read()
syn.close()

f = f.replace('.','')
f = f.replace(',','')

f = f.split(' ')
for dim in words:
    Synopsis.append(f.count(dim))
    
probs =[]

for i in range(0,19):
    temp = MLNB[i].predict_proba(Synopsis)[0]
    print temp
    if len(temp)==2:
        probs.append(MLNB[i].predict_proba(Synopsis)[0][1])
    else:
        probs.append(0)

Thres = sum(probs)/19
for i in range(0,19):
    if probs[i] >= Thres:
        print Lab[i]


raw_input('\nPress<Enter>')

from __future__ import division
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB

MLNB = [GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB(),GaussianNB()]

ftd = open('Training_Data.txt','r')
lines = ftd.readlines()
ftd.close()
features = []
Labels = []
Data = []
Synopsis = []
Dic = []

Lab = ['Adult','Action','Adventure','Animation','Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
Genres = []

for line in lines:
    line = line.split(' ')
    Labels.append(line[-19:])
    features.append(line[:-19])
    Dic = Dic + line[:-19]

Dic = list(set(Dic))
L = len(features)
for i in features:
    x = []
    for j in Dic:
        if j in i :
            x.append(1)
        else:
            x.append(0)
    Data.append(x)

for j in range(0,19):
    for i in Labels:
        y = []
        if i[j]=='0':
            y.append(1)
        else:
            y.append(0)
    Genres.append(y)
            
for i in range(0,19):
    MLNB[i].fit(Data,Genres[i])


syn = open('Synopsis.txt','r')
f = syn.read()
syn.close()
f = f.split(' ')
for dim in Dic:
    if dim in f:
        Synopsis.append(1)
    else:
        Synopsis.append(0)

probs =[]
for i in range(0,19):
    probs.append(MLNB[i].predict_proba(Synopsis)[0][1])

Thres = sum(probs)/19
for i in range(0,19):
    if probs[i] >= Thres:
        print Lab[i]


raw_input('\nPress<Enter>')

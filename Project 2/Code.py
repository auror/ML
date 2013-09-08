from __future__ import division
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
SVM = svm.SVC()
clf = GaussianNB()
Tree = tree.DecisionTreeClassifier()

f1 = open('Training.csv','r')
f2 = open('Testing.csv','r')

lines = f1.readlines()
Data = lines[0:601]
Test = lines[601:]
Data.pop(0)

Class = []
Predictions = []
PredictionsT = []
PredictionsS = []
Answers = []
for i in range(0,len(Data)):
    Data[i] = Data[i].split(',')
    Class.append(Data[i].pop(0))
    index = []
    for j in range(0,len(Data[i])):
        if '"' in Data[i][j]:
            index.append(Data[i].index(Data[i][j]))
    k = 0
    for x in index:
        Data[i].pop(x-k)
        k += 1
    Data[i].pop(3)
    Data[i].pop(3)
    Data[i].pop(3)
    Data[i].pop(4)
    Data[i].pop(4)
    Data[i].pop(3)

for i in range(0,len(Data)):
    if Data[i][2] != '':
        temp1 = int(Data[i][2])
    if Data[i][2]=='':
        Data[i][2] = 40
    else:
        Data[i][2] = temp1
   
    if Data[i][0]=='1':
        Data[i][0] = 1
    elif Data[i][0]=='2':
        Data[i][0] = 2
    else:
        Data[i][0] = 2
        
    if Data[i][1] == 'male':
        Data[i][1] = 0
    else:
        Data[i][1] = 1
    
Class = [int(x) for x in Class]
clf.fit(Data,Class)
Tree.fit(Data,Class)
SVM.fit(Data,Class)

for i in range(0,len(Test)):
    Test[i] = Test[i].split(',')
    Answers.append(Test[i].pop(0))
    index = []
    for j in range(0,len(Test[i])):
        if '"' in Test[i][j]:
            index.append(Test[i].index(Test[i][j]))
    k = 0
    for x in index:
        Test[i].pop(x-k)
        k += 1
    Test[i].pop(3)
    Test[i].pop(3)
    Test[i].pop(3)
    Test[i].pop(4)
    Test[i].pop(4)
    Test[i].pop(3)


for i in range(0,len(Test)):
    if Test[i][2] != '':
        temp1 = int(Test[i][2])
    if Test[i][2]=='':
        Test[i][2] = 40
    else:
        Test[i][2] = temp1
        
    if Test[i][0]=='1':
        Test[i][0] = 1
    elif Test[i][0]=='2':
        Test[i][0] = 2
    else:
        Test[i][0] = 2
        
    if Test[i][1] == 'male':
        Test[i][1] = 0
    else:
        Test[i][1] = 1

for item in Test:
    Predictions.append(clf.predict(item)[0])
    PredictionsT.append(Tree.predict(item)[0])
    PredictionsS.append(SVM.predict(item)[0])
    
Answers = [int(x) for x in Answers]    
f1.close()
f2.close()

count = 0
countT = 0
countS = 0

for a in range(0,len(Answers)):
    if Answers[a] == Predictions[a]:
        count += 1
    if Answers[a] == PredictionsT[a]:
        countT += 1
    if Answers[a] == PredictionsS[a]:
        countS += 1
          
print 'Accuracy of Naive-Bayes : ' + str(count*100/len(Answers)) + '\n'
print 'Accuracy of Decision Tree : ' + str(countT*100/len(Answers)) + '\n'
print 'Accuracy of Support Vector Machines : ' + str(countS*100/len(Answers)) + '\n'

raw_input('Press<Enter>')

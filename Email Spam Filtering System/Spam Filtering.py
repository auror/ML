from __future__ import division
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

BNB = BernoulliNB()
MNB = MultinomialNB()

f = open('SMSSpamTraining.txt','r')
lines = f.readlines()

Training = lines[0:800]
Test = lines[800:]
TrainingB = []
TrainingM = []
TestB = []
TestM = []
Labels = []
Features = []
Answers = []
PredictionsB = []
PredictionsM = []

for x in range(0,len(Training)):
    Training[x] = Training[x].split()
    Labels.append(Training[x].pop(0))
    Features += Training[x]

for x in range(0,len(Test)):
    Test[x] = Test[x].split()
    Answers.append(Test[x].pop(0))

Features = list(set(Features))

for x in Training:
    temp1 = []
    temp2 = []
    for y in Features:
        if y in x:
            temp1.append(1)
            temp2.append(x.count(y))
        else:
            temp1.append(0)
            temp2.append(0)
    TrainingB.append(temp1)
    TrainingM.append(temp2)

for x in Test:
    temp1 = []
    temp2 = []
    for y in Features:
        if y in x:
            temp1.append(1)
            temp2.append(x.count(y))
        else:
            temp1.append(0)
            temp2.append(0)
    TestB.append(temp1)
    TestM.append(temp2)

BNB.fit(TrainingB,Labels)
MNB.fit(TrainingM,Labels)

for x in TestB:
    PredictionsB.append(BNB.predict(x)[0])
for x in TestM:
    PredictionsM.append(MNB.predict(x)[0])

countB = 0
countM = 0

for i in range(0,len(PredictionsB)):
    if Answers[i] == PredictionsB[i]:
        countB += 1
    if Answers[i] == PredictionsM[i]:
        countM += 1

print 'Accuracy of Bernoulli Naive-Bayes : ' + str(countB*100/len(PredictionsB))
print 'Accuracy of Multinomial Naive-Bayes : ' + str(countM*100/len(PredictionsM))

raw_input('\nPress<Enter>')

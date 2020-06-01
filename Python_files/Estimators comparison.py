#linear SVC

from sklearn.datasets import make_classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import time
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

#importing set data and taget

#using RMS
af=pd.read_csv('grasp_10sec.csv')
grasp_10sec = af.ix[:,'emg1':'emg8']

bf=pd.read_csv('pinching_10sec.csv')
pinching_10sec = bf.ix[:,'emg1':'emg8']

cf=pd.read_csv('pointer_10sec.csv')
pointer_10sec = cf.ix[:,'emg1':'emg8']

df=pd.read_csv('rest_10sec.csv')
rest_10sec= df.ix[:,'emg1':'emg8']



X=[]
y=[]
i=0;
while i<1595:   
    y.append(1)
    X.append([grasp_10sec['emg1'][i],grasp_10sec['emg2'][i],grasp_10sec['emg3'][i],
      grasp_10sec['emg4'][i],grasp_10sec['emg5'][i],grasp_10sec['emg6'][i]
      ,grasp_10sec['emg7'][i],grasp_10sec['emg8'][i]])

    y.append(2)
    X.append([pinching_10sec['emg1'][i],pinching_10sec['emg2'][i],pinching_10sec['emg3'][i],
      pinching_10sec['emg4'][i],pinching_10sec['emg5'][i],pinching_10sec['emg6'][i]
      ,pinching_10sec['emg7'][i],pinching_10sec['emg8'][i]])

    y.append(3)
    X.append([pointer_10sec['emg1'][i],pointer_10sec['emg2'][i],
             pointer_10sec['emg3'][i],pointer_10sec['emg4'][i],
             pointer_10sec['emg5'][i],pointer_10sec['emg6'][i]
             ,pointer_10sec['emg7'][i],pointer_10sec['emg8'][i]])
    
    y.append(4)
    X.append([rest_10sec['emg1'][i],rest_10sec['emg2'][i],
             rest_10sec['emg3'][i],rest_10sec['emg4'][i],
             rest_10sec['emg5'][i],rest_10sec['emg6'][i]
             ,rest_10sec['emg7'][i],rest_10sec['emg8'][i]])

    
    i+=1

#Data has been loaded in the X and Y arrrays

    
# i need to use cross validation technique

#using linear SVC

from sklearn.model_selection import cross_val_score
clf = svm.SVC(kernel='linear', C=1)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  linear svc :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")
#using SVC OVO

from sklearn.model_selection import cross_val_score
clf = svm.SVC(decision_function_shape='ovo')
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for SVC OVO:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")
#using SVC ovr

from sklearn.model_selection import cross_val_score
clf = svm.SVC(decision_function_shape='ovr')
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for SVC ovr:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")
#using Nearest KNeighborsClassifier

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for KNeighborsClassifier:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using Forests of randomized tree classfier (tried)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for Forests of randomized tree classfier:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")


#using  Extremely Randomized Trees

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2,
    random_state=0)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for Decision tree classfier:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")
clf.fit(X,y)
joblib.dump(clf, 'Extra_tree_classfier.pkl')

clf = RandomForestClassifier(n_estimators=10, max_depth=None,
    min_samples_split=2, random_state=0)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for Random forest classfier:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,
    min_samples_split=2, random_state=0)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for ExtraTreesClassifier:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using GradientBoostingClassfier

from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
    max_depth=1, random_state=0)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for GradientBoostingClassfier:", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using  naive bayes Gaussian
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for Naive bayes Gaussian :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using BernoulliNB
#using  naive bayes Gaussian
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for Naive bayes BernoulliNB :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using MLP classfier
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  MLPClassifier :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")


#using NearestCentroid
from sklearn.neighbors.nearest_centroid import NearestCentroid
clf = NearestCentroid()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  NearestCentroid :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")


#using QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
clf = QuadraticDiscriminantAnalysis()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  QuadraticDiscriminantAnalysis :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")
#clf.fit(X,y)
#joblib.dump(clf, 'Quad.pkl')

#using NuSVC
from sklearn.svm import NuSVC
clf = NuSVC()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  NuSVC :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using PassiveAggressiveClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.datasets import make_classification
clf = PassiveAggressiveClassifier(random_state=0)
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  PassiveAggressiveClassifier :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")

#using SGD classfier
from sklearn.linear_model import SGDClassifier
clf = SGDClassifier(loss="log", penalty="l2")
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  SGD classfier :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")


#using linear model precption
import numpy as np
from sklearn import linear_model
clf = linear_model.SGDClassifier()
t0=time.time()
scores = cross_val_score(clf, X, y, cv=10)
print ("training time for  linear_model.SGDClassifier :", round(time.time()-t0, 5), "s")
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("")


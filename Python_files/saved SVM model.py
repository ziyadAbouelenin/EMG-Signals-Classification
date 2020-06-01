#Trainng data file
import csv
import pandas as pd
import math
import keyboard
import collections
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn import svm
from sklearn.externals import joblib



df=pd.read_csv('rest_10sec_Filtered_with_guessian_RMS.csv')
cf=pd.read_csv('grasp_10sec_filtered_and_RMS.csv')
pf=pd.read_csv('pointer_10sec_Filtered_with_guessian_RMS.csv')
hf=pd.read_csv('pinching_10sec_Filtered_with_guessian_RMS.csv')
# X -> features, y -> label
sensorsRest = df.ix[:,'emg1':'emg8']
sensorsFist = cf.ix[:,'emg1':'emg8']
sensorsPointer = pf.ix[:,'emg1':'emg8']
sensorsPenching = hf.ix[:,'emg1':'emg8']
# transferring them to arrays
i=0
X=[]
y=[]

while i<319 :
    y.append("rest")
    X.append([sensorsRest['emg1'][i],sensorsRest['emg2'][i],sensorsRest['emg3'][i],
      sensorsRest['emg4'][i],sensorsRest['emg5'][i],sensorsRest['emg6'][i]
      ,sensorsRest['emg7'][i],sensorsRest['emg8'][i]])

    y.append("grasping")
    X.append([sensorsFist['emg1'][i],sensorsFist['emg2'][i],sensorsFist['emg3'][i],
      sensorsFist['emg4'][i],sensorsFist['emg5'][i],sensorsFist['emg6'][i]
      ,sensorsFist['emg7'][i],sensorsFist['emg8'][i]])

    y.append("pointer")
    X.append([sensorsPointer['emg1'][i],sensorsPointer['emg2'][i],
             sensorsPointer['emg3'][i],sensorsPointer['emg4'][i],
             sensorsPointer['emg5'][i],sensorsPointer['emg6'][i]
             ,sensorsPointer['emg7'][i],sensorsPointer['emg8'][i]])
    y.append("3 finger grip")
    X.append([sensorsPenching['emg1'][i],sensorsPenching['emg2'][i],
             sensorsPenching['emg3'][i],sensorsPenching['emg4'][i],
             sensorsPenching['emg5'][i],sensorsPenching['emg6'][i]
             ,sensorsPenching['emg7'][i],sensorsPenching['emg8'][i]])
    i+=1
    

svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X, y) #SVM
joblib.dump(svm_model_linear, 'filtered.pkl')

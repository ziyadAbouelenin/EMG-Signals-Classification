# importing necessary libraries
from sklearn.model_selection import train_test_split
import pandas as pd
# importing data from csv files

#when using RMS+ threeshold the avg accuracy is 75
#when using raw data the avg accuracy is 45
df=pd.read_csv('rest-rms600sample.csv')
cf=pd.read_csv('grasp-rms600sample.csv')
pf=pd.read_csv('pointer-rms600sample.csv')
hf=pd.read_csv('penching-rms600sample.csv')
# X -> features, y -> label
sensorsRest = df.ix[:,'emg1':'emg8']
sensorsFist = cf.ix[:,'emg1':'emg8']
sensorsPointer = pf.ix[:,'emg1':'emg8']
sensorsPenching = hf.ix[:,'emg1':'emg8']
# transferring them to arrays
i=0
X=[]
y=[]

while i<len(sensorsRest):
    y.append("rest")
    X.append([sensorsRest['emg1'][i],sensorsRest['emg2'][i],sensorsRest['emg3'][i],
      sensorsRest['emg4'][i],sensorsRest['emg5'][i],sensorsRest['emg6'][i]
      ,sensorsRest['emg7'][i],sensorsRest['emg8'][i]])

    y.append("fist")
    X.append([sensorsFist['emg1'][i],sensorsFist['emg2'][i],sensorsFist['emg3'][i],
      sensorsFist['emg4'][i],sensorsFist['emg5'][i],sensorsFist['emg6'][i]
      ,sensorsFist['emg7'][i],sensorsFist['emg8'][i]])

    y.append("pointer")
    X.append([sensorsPointer['emg1'][i],sensorsPointer['emg2'][i],
             sensorsPointer['emg3'][i],sensorsPointer['emg4'][i],
             sensorsPointer['emg5'][i],sensorsPointer['emg6'][i]
             ,sensorsPointer['emg7'][i],sensorsPointer['emg8'][i]])
    y.append("penching")
    X.append([sensorsPenching['emg1'][i],sensorsPenching['emg2'][i],
             sensorsPenching['emg3'][i],sensorsPenching['emg4'][i],
             sensorsPenching['emg5'][i],sensorsPenching['emg6'][i]
             ,sensorsPenching['emg7'][i],sensorsPenching['emg8'][i]])
    y.append("writting")
    X.append([sensorsWritting['emg1'][i],sensorsWritting['emg2'][i],
             sensorsWritting['emg3'][i],sensorsWritting['emg4'][i],
             sensorsWritting['emg5'][i],sensorsWritting['emg6'][i]
             ,sensorsWritting['emg7'][i],sensorsWritting['emg8'][i]]) 
    i+=1






# training a linear SVM classifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline 


 
# training a KNN classifier
from sklearn.neighbors import KNeighborsClassifier


 
 
 
# training a Naive Bayes classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import mutual_info_classif

i=0
a=input("write the (segmantation frequancy-RMS segment-no of samples-time.txt) of the file precisly describing the data inside:")
m=n=k=0
'''
1- The result of offline training without RMS
2-The result of offline training with RMS 
3-The result of offline training with feature selection on Raw EMG data
4-The result of offline training with feature selection on EMG data+RMS
'''
while i<10:
    
    #with RMS and no feature selection
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = None)
    
    gnb = GaussianNB().fit(X_train, y_train)
    knn = KNeighborsClassifier(n_neighbors = 8).fit(X_train, y_train)
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
    '''
    #with RMS and with unvarient feature selection
    #_f_classif, mutual_info_classif
    
    X= SelectKBest(mutual_info_classif, k=5).fit_transform(X, y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = None)    
    gnb = GaussianNB().fit(X_train, y_train)
    knn = KNeighborsClassifier(n_neighbors = 8).fit(X_train, y_train)
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)    

    #----------------------------------------------------------------------
    m+=svm_model_linear.score(X_test, y_test)*100
    k+=knn.score(X_test, y_test)*100
    n+=gnb.score(X_test, y_test)*100
    with open(a, "a") as text_file:
        print(f"SVM accuracy is: {svm_model_linear.score(X_test, y_test)*100}", file=text_file)
        print(f"KNN accuracy is: {knn.score(X_test, y_test)*100}", file=text_file)
        print(f"Naive Bayes accuracy is: {gnb.score(X_test, y_test)*100}", file=text_file)
        print(f"--------------------------------\n", file=text_file)
    i+=1

with open(a, "a") as text_file:
        print(f"SVM  avg accuracy is: {m/10}", file=text_file)
        print(f"KNN avg accuracy is: {k/10}", file=text_file)
        print(f"Naive Bayes avg accuracy is: {n/10}", file=text_file)
        print(f"--------------------------------\n", file=text_file)
        
print("All is well!")    






    

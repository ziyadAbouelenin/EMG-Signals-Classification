from scipy.ndimage.filters import gaussian_filter
import pandas as pd
import csv
#importing set data and taget

#using RMS
af=pd.read_csv('grasping_new.csv')
GRASP = af.ix[:,'emg1':'emg8']



X=[]
y=[]
i=0;
emg1 = gaussian_filter(GRASP['emg1'], sigma=2)
emg2 = gaussian_filter(GRASP['emg2'], sigma=2)
emg3 = gaussian_filter(GRASP['emg3'], sigma=2)
emg4 = gaussian_filter(GRASP['emg4'], sigma=2)
emg5 = gaussian_filter(GRASP['emg5'], sigma=2)
emg6 = gaussian_filter(GRASP['emg6'], sigma=2)
emg7 = gaussian_filter(GRASP['emg7'], sigma=2)
emg8 = gaussian_filter(GRASP['emg8'], sigma=2)




r=input("file name:")
with open(r+".csv", 'a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['time','emg1','emg2','emg3'
                     ,'emg4','emg5','emg6','emg7','emg8'])

i=0
while i<len(emg1):
    with open(r+".csv", 'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([i,emg1[i],emg2[i],emg3[i], emg4[i],emg5[i],emg6[i] ,emg7[i],emg8[i]])
    i+=1    
    
    
    















    

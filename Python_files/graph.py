
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


af=pd.read_csv('grasp_10sec.csv')
grasp_10sec = af.ix[:,'time':'emg8']

bf=pd.read_csv('pinching_10sec.csv')
pinching_10sec = bf.ix[:,'emg1':'emg8']

cf=pd.read_csv('pointer_10sec.csv')
pointer_10sec = cf.ix[:,'emg1':'emg8']

df=pd.read_csv('rest_10sec.csv')
rest_10sec= df.ix[:,'emg1':'emg8']
a=a1=a2=a3=a4=a5=a6=a7=y=[]
for x in range(0,100):
    a+=[grasp_10sec['emg1'][x]]
    a1+=[grasp_10sec['emg2'][x]]
    a2+=[grasp_10sec['emg3'][x]]
    a3+=[grasp_10sec['emg4'][x]]
    a4+=[grasp_10sec['emg5'][x]]
    a5+=[grasp_10sec['emg6'][x]]
    a6+=[grasp_10sec['emg7'][x]]
    a7+=[grasp_10sec['emg8'][x]]
    y+=[x]

plt.figure()
plt.subplot(8,1,1)
plt.plot( y,a,'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 1')

plt.subplot(8,1,2)
plt.plot( y,a1,'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 2')

plt.subplot(8,1,3)
plt.plot( y,a2,'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 3')

plt.subplot(8,1,4)
plt.plot( y,a3,'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 4')

plt.subplot(8,1,5)
plt.plot( y,a4,'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 5')
'''
plt.subplot(226)
plt.plot( grasp_10sec['time'],grasp_10sec['emg6'],'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 6')

plt.subplot(227)
plt.plot( grasp_10sec['time'],grasp_10sec['emg7'],'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 7')

plt.subplot(228)
plt.plot( grasp_10sec['time'],grasp_10sec['emg8'],'b')
plt.grid(True)
plt.title('Raw EMG data for sensor 8')
'''
plt.show()

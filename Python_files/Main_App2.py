import csv
import pandas as pd
import math
import myo
import threading
import keyboard
import collections
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn import svm
import serial
from sklearn.externals import joblib     
import time
ser = serial.Serial('COM7', 9600)

#data Fitting
#gnb = GaussianNB().fit(X, y) #NaiveBayes
svm_model_linear = joblib.load('savedModel.pkl')
print("press cntrl to see real time data!")

#knn = KNeighborsClassifier(n_neighbors = 8).fit(X, y)#knn


#applying root mean square to data before writting it to csv:
def avg(number,count):
    return number/count

def square(e,data):
  return e+math.pow(data,2)
r=5
def RMS(data):#take list sample number and counter
    result=[]
    i=e=e1=e2=e3=e4=e5=e6=e7=0
    while i < r:
      e=square(e,data[i][0])
      e1=square(e1,data[i][1])
      e2=square(e2,data[i][2])
      e3=square(e3,data[i][3])
      e4=square(e4,data[i][4])
      e5=square(e5,data[i][5])
      e6=square(e6,data[i][6])
      e7=square(e7,data[i][7])
      i+=1
    e=math.sqrt(avg(e,r))
    e1=math.sqrt(avg(e1,r))
    e2=math.sqrt(avg(e2,r))
    e3=math.sqrt(avg(e3,r))
    e4=math.sqrt(avg(e4,r))
    e5=math.sqrt(avg(e5,r))
    e6=math.sqrt(avg(e6,r))
    e7=math.sqrt(avg(e7,r))
    result.append(e)
    result.append(e1)
    result.append(e2)
    result.append(e3)
    result.append(e4)
    result.append(e5)
    result.append(e6)
    result.append(e7)
    return(result)
    
        
class MyListener(myo.DeviceListener):
    

  def __init__(self,queue_size=8):
    self.lock = threading.Lock()
    self.emg_data_queue = collections.deque(maxlen=queue_size)
    self.gyro_data_queue = collections.deque(maxlen=3)
    self.ori_data_queue = collections.deque(maxlen=4)
    self.acc_data_queue = collections.deque(maxlen=3)
                                             
  def on_connect(self, device, timestamp, firmware_version):
    device.set_stream_emg(myo.StreamEmg.enabled)

  
  def on_emg_data(self, device, timestamp, emg_data):
    with self.lock:
      for x in range(0,8):
        self.emg_data_queue.append((emg_data[x]))
        
  def get_emg_data(self):
    with self.lock:
      return list(self.emg_data_queue)
    



 
a=v=[]
flag=False
n=0
myo.init(r'C:\Users\Ziyad Elshafei\Desktop\myo-sdk-win-0.9.0\bin')
hub = myo.Hub()
try:
  listener = MyListener()
  hub.run(200, listener)
  while True:
    if(flag):
      a.append(listener.get_emg_data())
      n+=1
      if(n==r):
          v=RMS(a)
          #n=gnb.predict([[v[0],v[1], v[2],v[3],v[4],v[5],v[6] ,v[7]]])
          s=svm_model_linear.predict([[v[0],v[1], v[2],v[3],v[4],v[5],v[6] ,v[7]]])
          #k=knn.predict([[v[0],v[1], v[2],v[3],v[4],v[5],v[6] ,v[7]]])
          #print("   SVM predicted:  ",s ,"           Naive Beyes predicted:  ",n,"                         Knn predicted:  ",k)
          print("                                     ",s)
          
          if (s=="grasping"):
              ser.write(b'1')
          if (s=="rest"):
              ser.write(b'0')              
          if (s=="3 finger grip"):
              ser.write(b'3')
          if (s=="pointer"):
              ser.write(b'2')
          
              
          a=[]
          n=0
          
    time.sleep(0.1)#0.0005
    if keyboard.is_pressed('ctrl'):
        flag=True
        print("ctrl was pressed")
    if keyboard.is_pressed('shift'):
        flag=False
    if keyboard.is_pressed('esc'):
        break
finally:
  hub.shutdown()




#Note as data increased this model fails to work as intended i.e many mistakes took place 
#let me increase samples to 1000 and use differnt models

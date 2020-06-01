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
from sklearn.externals import joblib     
import time
from scipy.ndimage.filters import gaussian_filter

svm_model_linear = joblib.load('filtered.pkl')
print("press cntrl to see real time data!")



#applying root mean square to data before writting it to csv:
def avg(number,count):
    return number/count

def square(e,data):
    return e+math.pow(data,2)
def RMS(data):#take list sample number and counter
    result=[]
    i=e=e1=e2=e3=e4=e5=e6=e7=0
    while i < 5:
        e=square(e,data[i][0])
        e1=square(e1,data[i][1])
        e2=square(e2,data[i][2])
        e3=square(e3,data[i][3])
        e4=square(e4,data[i][4])
        e5=square(e5,data[i][5])
        e6=square(e6,data[i][6])
        e7=square(e7,data[i][7])
        i+=1
    e=math.sqrt(avg(e,5))
    e1=math.sqrt(avg(e1,5))
    e2=math.sqrt(avg(e2,5))
    e3=math.sqrt(avg(e3,5))
    e4=math.sqrt(avg(e4,5))
    e5=math.sqrt(avg(e5,5))
    e6=math.sqrt(avg(e6,5))
    e7=math.sqrt(avg(e7,5))
    result.append(e)
    result.append(e1)
    result.append(e2)
    result.append(e3)
    result.append(e4)
    result.append(e5)
    result.append(e6)
    result.append(e7)
    return(result)

def Filter(data):
    o=[]
    z1=z2=z3=z4=z5=z6=z7=z8=[]
    z1=gaussian_filter([data[0][0],data[1][0],data[2][0], data[3][0],data[4][0]], sigma=2)
    z2=gaussian_filter([data[0][1],data[1][1],data[2][1], data[3][1],data[4][1]], sigma=2)
    z3=gaussian_filter([data[0][2],data[1][2],data[2][2], data[3][2],data[4][2]], sigma=2)
    z4=gaussian_filter([data[0][3],data[1][3],data[2][3], data[3][3],data[4][3]], sigma=2)
    z5=gaussian_filter([data[0][4],data[1][4],data[2][4], data[3][4],data[4][4]], sigma=2)
    z6=gaussian_filter([data[0][5],data[1][5],data[2][5], data[3][5],data[4][5]], sigma=2)
    z7=gaussian_filter([data[0][6],data[1][6],data[2][6], data[3][6],data[4][6]], sigma=2)
    z8=gaussian_filter([data[0][7],data[1][7],data[2][7], data[3][7],data[4][7]], sigma=2)
    o=[ [ z1[0],z2[0],z3[0],z4[0],z5[0],z6[0],z7[0],z8[0] ]
        ,[z1[1],z2[1],z3[1],z4[1],z5[1],z6[1],z7[1],z8[1]]
        ,[z1[2],z2[2],z3[2],z4[2],z5[2],z6[2],z7[2],z8[2]]
        ,[z1[3],z2[3],z3[3],z4[3],z5[3],z6[3],z7[3],z8[3]],[z1[4],z2[4],z3[4],z4[4],z5[4],z6[4],z7[4],z8[4]] ]
    return(o)
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
counter=0
true=0
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
      if(n==5):
          v=RMS(Filter(a))
          
          s=svm_model_linear.predict([v])
          print("                                     ",s, "", counter)
          if (s=="pointer"):
              true+=1
          
          a=[]
          n=0
          
    time.sleep(0.1)#0.0005
    if keyboard.is_pressed('ctrl'):
        flag=True
        print("ctrl was pressed")
    if keyboard.is_pressed('shift'):
        flag=False
    if keyboard.is_pressed('esc'):
        print((true*100)/counter)
        break
finally:
  hub.shutdown()



#Note as data increased this model fails to work as intended i.e many mistakes took place 
#let me increase samples to 1000 and use differnt models

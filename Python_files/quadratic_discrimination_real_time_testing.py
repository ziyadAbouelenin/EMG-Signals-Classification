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

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

#svm_model_linear = joblib.load('filtered.pkl')
clf=joblib.load('Quad.pkl')
print("press cntrl to see real time data!")

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
s=0
# real time accuracy

myo.init(r'C:\Users\Ziyad Elshafei\Desktop\myo-sdk-win-0.9.0\bin')
hub = myo.Hub()
try:
  listener = MyListener()
  hub.run(200, listener)
  while True:
      if flag==True:
          a.append(listener.get_emg_data())
          s=clf.predict(a)
          if s==1:
              print("                                     ", " GRASPING")
          if s==2:
              print("                                     ", " PINCHING")
          if s==3:
              print("                                     ", " POINTER")
          if s==4:
              print("                                     ", " REST")              
          a=[]
          counter+=1
          if (s== 4    ):
              true+=1
          
      time.sleep(0.0005)#0.0005
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

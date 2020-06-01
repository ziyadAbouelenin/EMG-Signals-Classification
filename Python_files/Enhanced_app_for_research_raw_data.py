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

#data Fitting

svm_model_linear = joblib.load('raw.pkl')
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
    



 
a=[]
counter=0
true=0
flag=False
myo.init(r'C:\Users\Ziyad Elshafei\Desktop\myo-sdk-win-0.9.0\bin')
hub = myo.Hub()
try:
  listener = MyListener()
  hub.run(200, listener)
  while True:
      if(flag):
          counter+=1
          a.append(listener.get_emg_data())
          s=svm_model_linear.predict(a)
          print("                                     ",s, "", counter)
          if (s=="3 finger grip"):
              true+=1
          
          a=[]
      time.sleep(0.0005)#0.0005
      if keyboard.is_pressed('ctrl'):
          flag=True
          print("ctrl was pressed")
      if keyboard.is_pressed('esc'):
          print((true*100)/counter)
          break
finally:
  hub.shutdown()




#Note as data increased this model fails to work as intended i.e many mistakes took place 
#let me increase samples to 1000 and use differnt models

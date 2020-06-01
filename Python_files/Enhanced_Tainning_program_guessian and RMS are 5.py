#use the following command in cmd
# python Trainng_program.py build
import csv
import pandas as pd
import math
import myo
import threading
import keyboard
import collections
import time
from scipy.ndimage.filters import gaussian_filter
print("please enter the (pose) you are performing)  : ")
e=input()
n=e+".csv"
s=True

print("Got u! keep pressing (alt) while you performe this gesture")
print("when you are done press (shift) to write the filtered data  in csv files")

with open(n, 'a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['time','emg1','emg2','emg3'
                     ,'emg4','emg5','emg6','emg7','emg8',])
def EMGfiles(emg,t):
    with open(n, 'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow([t,emg[0],emg[1],emg[2],
                         emg[3],emg[4],emg[5],emg[6],emg[7]])


#applying root mean square to data before writting it to csv:
def avg(number,count):
    return number/count

def Filter(data,segment):#take list sample number and counter
    i=c=0
    z=z1=z2=z3=z4=z5=z6=z7=[]
    print("wait I am applying the guessian filter to your data")
    r=e+"_Filtered_with_guessian_2.csv"
    with open(r, 'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['time','emg1','emg2','emg3'
                         ,'emg4','emg5','emg6','emg7','emg8'])
    while segment <= len(data):
        z=gaussian_filter([data[i][0],data[i+1][0],data[i+2][0], data[i+3][0],data[i+4][0]], sigma=2)
        z1=gaussian_filter([data[i][1],data[i+1][1],data[i+2][1], data[i+3][1],data[i+4][1]], sigma=2)
        z2=gaussian_filter([data[i][2],data[i+1][2],data[i+2][2], data[i+3][2],data[i+4][2]], sigma=2)
        z3=gaussian_filter([data[i][3],data[i+1][3],data[i+2][3], data[i+3][3],data[i+4][3]], sigma=2)
        z4=gaussian_filter([data[i][4],data[i+1][4],data[i+2][4], data[i+3][4],data[i+4][4]], sigma=2)
        z5=gaussian_filter([data[i][5],data[i+1][5],data[i+2][5], data[i+3][5],data[i+4][5]], sigma=2)
        z6=gaussian_filter([data[i][6],data[i+1][6],data[i+2][6], data[i+3][6],data[i+4][6]], sigma=2)
        z7=gaussian_filter([data[i][7],data[i+1][7],data[i+2][7], data[i+3][7],data[i+4][7]], sigma=2)
        
        segment+=5
        i=segment-5

        for x in range(0,5):
            with open(r, 'a',newline='') as f:
                writer=csv.writer(f)
                writer.writerow([t[c],z[x],z1[x],z2[x],z3[x],z4[x],z5[x],z6[x],z7[x]])
            c+=1
        
    
        z=z1=z2=z3=z4=z5=z6=z7=[]  
    print("Filter csv finished writting go and see it!")
    print("press esc to exit")
    


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
    
  def on_gyroscope_data(self, device, timestamp, gyroscope):
          with self.lock:
              self.gyro_data_queue.append((gyroscope.x))
              self.gyro_data_queue.append((gyroscope.y))
              self.gyro_data_queue.append((gyroscope.z))
              
  def on_orientation_data(self, myo, timestamp, quat):
      with self.lock:
          self.ori_data_queue.append((quat.x))
          self.ori_data_queue.append((quat.y))
          self.ori_data_queue.append((quat.z))
          self.ori_data_queue.append((quat.w)) 

  def get_gyro_data(self):
      with self.lock:
            return list(self.gyro_data_queue)

  def get_ori_data(self):
      with self.lock:
            return list(self.ori_data_queue)      
  def on_accelerometor_data(self, device, timestamp, acceleration):
      with self.lock:
          self.acc_data_queue.append((acceleration.x))
          self.acc_data_queue.append((acceleration.y))
          self.acc_data_queue.append((acceleration.z))
 
  def get_acc_data(self):
      with self.lock:
            return list(self.acc_data_queue)
 
a=[]
t=[]
f=0
myo.init(r'C:\Users\Ziyad Elshafei\Desktop\myo-sdk-win-0.9.0\bin')
hub = myo.Hub()
try:
  listener = MyListener()
  hub.run(200, listener)

  while True:                                

      if keyboard.is_pressed('alt'):
          EMGfiles(listener.get_emg_data(),f)
          a.append(listener.get_emg_data())
          t.append(f)
          f+=1

      if keyboard.is_pressed('shift'):
          Filter(a,5)# write your segment number here
          #GYROfiles(listener.get_gyro_data())
         # ORIfiles(listener.get_ori_data())
          #ACCfiles(listener.get_acc_data())
          
          #print(listener.get_acc_data())
         #a= listener.get_gyro_data()
          #b=listener.get_acc_data()
         # c=listener.get_emg_data()
      if keyboard.is_pressed('esc'):
          break
      time.sleep(0.0005 )#50hz EMG(0.016) 200 hz (0.0005)
finally:
        hub.shutdown()


#Note as data increased this model fails to work as intended i.e many mistakes took place 
#let me increase samples to 1000 and use differnt models

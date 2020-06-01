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
print("please enter the (pose) you are performing)  : ")
e=input()
n=e+".csv"

#segmentation number
h = 5                    #int(input("Enter a number of rms sgmentation: "))

print("Got u! keep pressing (alt) while you performe this gesture")
print("when you are done press (shift) to write RMS of your data in csv files")

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

def RMS(data,segment):#take list sample number and counter
    i=c=a=a1=a2=a3=a4=a5=a6=a7=0
    print("wait I am applying the RMS filter to your data")
    r=e+"_RMS.csv"
    with open(r, 'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['time','emg1','emg2','emg3'
                         ,'emg4','emg5','emg6','emg7','emg8'])
    while segment < len(data):
        while i<segment:
            a=a+math.pow(data[i][0],2)
            a1=a1+math.pow(data[i][1],2)
            a2=a2+math.pow(data[i][2],2)
            a3=a3+math.pow(data[i][3],2)
            a4=a4+math.pow(data[i][4],2)
            a5=a5+math.pow(data[i][5],2)
            a6=a6+math.pow(data[i][6],2)
            a7=a7+math.pow(data[i][7],2)
            i+=1
        segment+=h
        i=segment-h
        with open(r, 'a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([t[c],math.sqrt(avg(a,h)),
                             math.sqrt(avg(a1,h)),math.sqrt(avg(a2,h)),
                         math.sqrt(avg(a3,h)),math.sqrt(avg(a4,h)),
                             math.sqrt(avg(a5,h)),math.sqrt(avg(a6,h)),
                             math.sqrt(avg(a7,h))])
        c+=1
        a=a1=a2=a3=a4=a5=a6=a7=0
        
    print("RMS csv finished writting go and see it!")
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
          RMS(a,h)# write your segment number here
          
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

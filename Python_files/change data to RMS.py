import csv
import pandas as pd
#importing set data and taget
import math

af=pd.read_csv('pointer_10sec.csv')
grasp_10sec = af.ix[:,'emg1':'emg8']
X=[]
i=0;
while i<1600:   #1450
    X.append([grasp_10sec['emg1'][i],grasp_10sec['emg2'][i],grasp_10sec['emg3'][i],
      grasp_10sec['emg4'][i],grasp_10sec['emg5'][i],grasp_10sec['emg6'][i]
      ,grasp_10sec['emg7'][i],grasp_10sec['emg8'][i]])
    i+=1
    
def avg(number,count):
    return number/count

def RMS(data,segment):#take list sample number and counter
    i=c=a=a1=a2=a3=a4=a5=a6=a7=0
    print("write the file name.csv for RMS data")
    r=input()
    with open(r+".csv", 'a',newline='') as f:
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
        segment+=5
        i=segment-5
        with open(r+".csv", 'a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([c,math.sqrt(avg(a,5)),
                             math.sqrt(avg(a1,5)),math.sqrt(avg(a2,5)),
                         math.sqrt(avg(a3,5)),math.sqrt(avg(a4,5)),
                             math.sqrt(avg(a5,5)),math.sqrt(avg(a6,5)),
                             math.sqrt(avg(a7,5))])
        c+=1
        a=a1=a2=a3=a4=a5=a6=a7=0
        
RMS(X,5)
print("RMS csv finished writting go and see it!")

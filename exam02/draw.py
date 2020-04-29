import matplotlib.pyplot as plt

import numpy as np

import serial
import time
Fs=100;
Ts=10.0/Fs;
t= np.arange(0,10,Ts) 
x= np.arange(0,10,Ts) 
y = np.arange(0,10,Ts) 
z = np.arange(0,10,Ts) 
event = np.arange(0,10,Ts) 

serdev='/dev/ttyACM0'
s = serial.Serial(serdev,115200)



for i in range(0,(4*int(Fs))):
    line=s.readline()
    if(i%4==0):
        k=int((i-i%4)/4)
        x[k]=float(line)
    if(i%4==1):
        k=int((i-i%4)/4)
        y[k]=float(line)     
    if(i%4==2):
        k=int((i-i%4)/4)
        z[k]=float(line)    
    if(i%4==3):
        k=int((i-i%4)/4)
        event[k]=float(line) 


plt.subplot(2,1,1)    
l1, =plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("acc vector")
l2, =plt.plot(t,y)
l3, =plt.plot(t,z)
plt.legend(handles=[l1,l2,l3],labels=['x_acc','y_acc','z_acc'],loc="lower left")

plt.subplot(2,1,2)
plt.plot(t,event,'ob')
plt.xlabel("time")
plt.ylabel("event")
plt.show()
s.close()
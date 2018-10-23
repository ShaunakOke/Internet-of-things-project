import RPi.GPIO as GPIO
from picamera import PiCamera
from random import randint
import thread
import threading
import socket
import time
from time import sleep
import os
import base64
import decrypt
import decrypt2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
GPIO.setup(07, GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
pwm2=GPIO.PWM(36,50)
pwm=GPIO.PWM(07, 100)


port=23000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('',port))
except socket.error as e:
        print(str(e))
s.listen(10)
	
li_flag=0
fan_flag=0
door_flag=0
GetCmd=0
var=0

def init(c):
	
	#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("Connected to "+str(addr))
	a=1
	while a==1:
		m=10
		m=int(c.recv(1024))
		print("Value of M outside")
		print(m)
		if m==1:
			print("username menu")
			u=c.recv(1024)
			u=u.strip()
			p=c.recv(1024)
			p=p.strip()
			print(u)
			#print(p)
			o=decrypt2.decrypt()
			u2=o.decryptaes(u)
			u2=u2.strip()
			print(u2)
			print(p)
			o2=decrypt2.decrypt()
			print('Object created')
			p2=o2.decryptaes(p)
			p2=p2.strip()
			print(p2)
			keypair=u2+"-"+p2
			filen="db2.txt"
			fo=open(filen,"r")
			var="No"
			for line in fo:
				if line.strip()==keypair :
					var="Yes"
					
			fo.close()
			print(var)
			#time.sleep(3)
			c.sendall(var+"\n")
			print("done sending")
			
			u=None
			p=None
			u2=None
			p2=None
			o=None
			o2=None
			var=None
			

		elif m==2:
			
			l=int(c.recv(1024))
			print("Value of L")
		        print(l)
			if(l==1):
	                	GPIO.output(11, 1)
	                	
			elif(l==2):
	                	GPIO.output(11, 0)
	                	
			elif(l==3):
				pwm.start(0)
				GPIO.output(03, True)
				GPIO.output(05, False)
				pwm.ChangeDutyCycle(15)
				GPIO.output(07, True)
			elif(l==4):
				GPIO.output(07, False)
				pwm.stop()
			
			elif(l==5):
				pwm2.start(0)
				GPIO.output(36,True)
				pwm2.ChangeDutyCycle(6)
				
				
				
				GPIO.output(36,False)		
				pwm2.stop()
			elif(l==6):
				pwm2.start(0)
				GPIO.output(36,True)
		       		pwm2.ChangeDutyCycle(2)
				GPIO.output(36,False)
        			pwm2.stop()
                elif m==3:
                        print("Add username")
			u=c.recv(1024)
			u=u.strip()
			p=c.recv(1024)
			p=p.strip()
			o=decrypt2.decrypt()
			u2=o.decryptaes(u)
			u2=u2.strip()
			print(u2)
			print(p)
			o2=decrypt2.decrypt()
			print('Object created')
			p2=o2.decryptaes(p)
			p2=p2.strip()
                    
                        filen="db2.txt"
                        fo=open(filen,"a+")
                        lis=[]
			print(u2)
			print(p2)
                        lis.append(u2)
                        lis.append("-"+p2)
                        print lis
                        fo.writelines(lis)
                        fo.write("\n")
                        fo.close()
			
                        
                        
                elif m==4:
			print("delete menu")
			u=c.recv(1024)
			u=u.strip()
			p=c.recv(1024)
			p=p.strip()
			print(u)
			#print(p)
			o=decrypt2.decrypt()
			u2=o.decryptaes(u)
			u2=u2.strip()
			print(u2)
			print(p)
			o2=decrypt2.decrypt()
			print('Object created')
			p2=o2.decryptaes(p)
			p2=p2.strip()
			print(p2)
			keypair=u2+"-"+p2
			filen="db2.txt"
			fo=open(filen,"r")
			lis=fo.readlines()
			print (lis)
			for ind, line in enumerate(lis):
				if line.strip()==keypair :
					lis[ind]=""
			fo.close()
			fo=open(filen,"w")
			fo.writelines(lis)
			    
			fo.close()
		
		elif m==5:
			print("admin verification")
			u=c.recv(1024)
			u=u.strip()
			p=c.recv(1024)
			p=p.strip()
			o=decrypt2.decrypt()
			u2=o.decryptaes(u)
			u2=u2.strip()
			print(u2)
			print(p)
			o2=decrypt2.decrypt()
			print('Object created')
			p2=o2.decryptaes(p)
			p2=p2.strip()
			print(p2)
			keypair=u2+"-"+p2
			filen="db.txt"
			var="No"
			fo=open(filen,"r")
			for line in fo:
				if line.strip()==keypair :
					var="Yes"
					
			fo.close()
			print(var)
			#time.sleep(3)
			c.sendall(var+"\n")
			print("done sending")
			
			u=None
			p=None
			u2=None
			p2=None
			o=None
			o2=None
			var=None

		elif m==6:
			print("admin change")
			u=c.recv(1024)
			u=u.strip()
			p=c.recv(1024)
			p=p.strip()
			print(u)
			#print(p)
			o=decrypt2.decrypt()
			u2=o.decryptaes(u)
			u2=u2.strip()
			print(u2)
			print(p)
			o2=decrypt2.decrypt()
			print('Object created')
			p2=o2.decryptaes(p)
			p2=p2.strip()
			print(p2)
			keypair=u2+"-"+p2
			filen="db.txt"
                        fo=open(filen,"w")
                        lis=[]
			print(u2)
			print(p2)
                        lis.append(keypair)
                        print lis
                        fo.writelines(lis)
                        fo.write("\n")
                        fo.close()
			
			u=None
			p=None
			u2=None
			p2=None
			o=None
			o2=None
			var=None
		m=10
          
			
	c.close()


while True:
	c,addr=s.accept()
	print ("New thread start")
	thread.start_new_thread(init,(c,))
	
	
	

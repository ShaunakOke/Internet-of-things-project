import time
import RPi.GPIO as GPIO
import os
import way2sms

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

while True:
	i=GPIO.input(13)
	if(i==1):
		print "Motion"
		os.system("raspistill -o image.jpg")
		q=way2sms.sms("7038792582","Q2253R")
		q.send(7038792582,"Intruder has been detected, please check mail")
		print "Message sent"
		os.system("python sendimg.py")	
		print "Email sent"

		q.logout()
		
		
	else:
		GPIO.output(11, 0)
		print "no motion"
	time.sleep(0.5)
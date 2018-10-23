import time, sys
import RPi.GPIO as GPIO
import way2sms
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT)
def action(pin):
	print('Sensor detected action!')
	q=way2sms.sms("7038792582","Q2253R")
	q.send(7038792582,"SMOKE HAS BEEN DETECTED")
	GPIO.output(12, 1)
	
	GPIO.output(12, 0)
	return
 
GPIO.add_event_detect(22, GPIO.RISING)
GPIO.add_event_callback(22, action)
 
try:
    while True:
        GPIO.output(12, 0)
        print('alive')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.output(12, 0)
    GPIO.cleanup()
    sys.exit()

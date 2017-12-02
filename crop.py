#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import paho.mqtt.client as paho
import time





client = paho.Client()
client.connect("broker.hivemq.com", 1883)
client.loop_start()

sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(23, GPIO.IN)         #Read output for Flame sensor
GPIO.setup(26, GPIO.OUT)
pin = 3
while True:

        i=GPIO.input(21)
j=GPIO.input(20)
        k=GPIO.input(16)
        l=GPIO.input(4)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
                        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))



        else:
                        print('Failed to get reading. Try again!')

        if i==1:                 #When output from motion sensor is LOW
                        print "no fire"
                        time.sleep(0.1)
                        GPIO.output(26,1)
                        a=0

        elif i==0:               #When output from motion sensor is HIGH
                        print "fire detected"
                        time.sleep(0.1)
                        a=1
                        GPIO.output(26,0)
        if j==1:                 #When output from motion sensor is LOW
                        print "No animal"
                        time.sleep(0.1)
                        b=0
        elif j==0:               #When output from motion sensor is HIGH

 						print "Animals detected"
                        time.sleep(0.1)
                        b=1

        if k==1:
                        print "no gas detected"
                        c=0

        elif k==0:
                        print"gas detected."
                        c=1

        if l==1:
                        print "moisture is low"
                        d=0
                        GPIO.output(19,0)
        elif l==0:
                        print "moisture level ok"
                        d=1
                        GPIO.output(19,1)
 

	    data=str(humidity)+str(temperature)+str(a)+str(b)+str(c)+str(d)
        client.publish("/cropcap1",data)




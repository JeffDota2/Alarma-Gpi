#Aqui llamamos a las biblitecas y los puetos
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# asctivamos las gpio de las rasperry
GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) 

try:
    time.sleep(2) 
    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(0.5) #un queño bucle de 0.5 segundos
            GPIO.output(24, False)
            print("Motion Detected...")#imprimo si detecto o no
            time.sleep(5)  
        time.sleep(0.1) 

except:
    GPIO.cleanup()
import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11
      PIN_Buzz = 15

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)
      GPIO.setup(PIN_Buzz, GPIO.OUT, initial=GPIO.LOW)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      # time for sensor to adjust

      time.sleep(2)
      pwm = GPIO.PWM(PIN_Buzz, 100)
      pwm.start(0)

      while(True):

            print "Calculating distance"

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)
            time.sleep(0.00001)                            # send trigger pulse signal
            GPIO.output(PIN_TRIGGER, GPIO.LOW)


            while GPIO.input(PIN_ECHO)==0:
                  pulse_start_time = time.time()            #Capture pulse from the start to finish via echo
            while GPIO.input(PIN_ECHO)==1:                  #via the GPIO.input from the echo pin
                  pulse_end_time = time.time()               #time it. and save the times


            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)           #the math to calculate the distance of an object
                        
                        #print distance 
            print "Distance:",distance,"cm"

            #buzzer pin feedback
            if (distance <= 110):
                  pwm.ChangeFrequency(12 - distance / 10)
                  pwm.ChangeDutyCycle(50)
                  time.sleep(1)
            else:
                  pwm.ChangeDutyCycle(0)      
            

except KeyboardInterrupt:
      GPIO.cleanup()
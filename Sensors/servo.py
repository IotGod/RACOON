import RPi.GPIO as GPIO
from time import sleep

SERVO_PIN = 18
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)


def lockDoor():
    pwm=GPIO.PWM(SERVO_PIN, 50)
    pwm.start(0)
    
    duty = 0 / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)
    
    pwm.stop()
    GPIO.cleanup()
    
    return 0

def unlockDoor():
    pwm=GPIO.PWM(SERVO_PIN, 50)
    pwm.start(0)
    
    duty = 180 / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)
    
    pwm.stop()
    GPIO.cleanup()
    
    return 0

if __name__ == "__main__":
    lockDoor()
    sleep(1)
    unlockDoor()
    sleep(1)
    lockDoor()

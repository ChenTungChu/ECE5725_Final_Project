import RPi.GPIO as GPIO
import time
import sys

global p_left
global p_right

def callback(channel):
    global p_left
    global p_right
    if channel == 17:
        print("Stopped!")
        p_left.stop()
        p_right.stop()
        GPIO.cleanup()
        sys.exit(0)


def main():
    global p_left, p_right
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(17, GPIO.FALLING, callback=callback, bouncetime=300)
    
    
    output_gpio = (5, 6, 16, 20, 21, 26)
    for b in output_gpio: GPIO.setup(b, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH) # PWMA
    GPIO.output(16, GPIO.HIGH) # PWMB

    # try setting
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    # PWM B
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    
    p_left = GPIO.PWM(26, 50)   # PWMA
    p_right = GPIO.PWM(16, 50)  # PWMB 
    
    p_left.start(45) # actually right motor 
    p_right.start(45)
    
    start_time = time.time()
    while True:
        if time.time() - start_time > 30:
            p_left.stop()
            p_right.stop()
            GPIO.cleanup()
            sys.exit(0)
            
            
            
if __name__ == "__main__":
    main()
    
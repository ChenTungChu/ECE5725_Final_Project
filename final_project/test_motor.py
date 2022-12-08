import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    output_gpio = (5, 6, 16, 20, 21, 26)
    for b in output_gpio: GPIO.setup(b, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH) # PWMA
    GPIO.output(16, GPIO.HIGH) # PWMB

    # try setting
    GPIO.output(6, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)
    
    p_left = GPIO.PWM(26, 50)   # PWMA
    p_right = GPIO.PWM(16, 50)  # PWMB 
    
    p_left.start(45)
    p_right.start(45)
    
    start_time = time.time()
    while True:
        if time.time() - start_time > 120:
            p_left.stop()
            p_right.stop()
            sys.exit(0)
            
            
            
if __name__ == "__main__":
    main()
    
import RPi.GPIO as GPIO
import time

Buzzer = 31
LED = 32
Button = 7

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Buzzer, GPIO.OUT)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while True:
            if GPIO.input(Button) == 0:
                GPIO.output(LED, False)
                GPIO.output(Buzzer, False)
            else:
                GPIO.output(LED, True)
                GPIO.output(Buzzer, True)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()

import Adafruit_CharLCD as LCD # https://github.com/adafruit/Adafruit_Python_CharLCD
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
lcd1 = 12
lcd2 = 7
lcd3 = 8
lcd4 = 25
lcd5 = 24
lcd6 = 23
trig = 17 # trig pin of ultrasonic sensor to GPIO 17 of the RPi
echo = 27 # echo pin of ultrasonic sensor to GPIO 27 of the RPi
lcd = LCD.Adafruit_CharLCD(lcd1, lcd2, lcd3, lcd4, lcd5, lcd6, 0, 16, 2)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
while True:
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo) == 0:
        pulse_s = time.time()
    while GPIO.input(echo) == 1:
        pulse_e = time.time()
    pulse_duration = pulse_e - pulse_s
    d = int(34000*pulse_duration/2)
    print(d)
    k = str(d)
    lcd.message('Distance:')
    lcd.message(k)
    lcd.message(" cm")
    time.sleep(0.5)
    lcd.clear()
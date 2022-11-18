import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led_pin = 7

GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.LOW)


for x in range(20):
	GPIO.output(led_pin, GPIO.HIGH)
	print("Pin High")
	time.sleep(2)

	GPIO.output(led_pin, GPIO.LOW)
	print("Pin Low")
	time.sleep(2)
	


GPIO.cleanup()

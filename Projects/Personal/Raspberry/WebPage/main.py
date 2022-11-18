import RPi.GPIO as GPIO
from flask import Flask

def gpio_start():
	global LED_PIN 
	LED_PIN = 7
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED_PIN, GPIO.OUT)


app = Flask(__name__)

@app.route("/HIGH")
def set_high():
	GPIO.output(LED_PIN, GPIO.HIGH)

@app.route("/LOW")
def set_low():
	GPIO.output(LED_PIN, GPIO.LOW)


if __name__ == "__main__":
	gpio_start()
	app.run(host = "0.0.0.0", port=int("5000"), debug=True)


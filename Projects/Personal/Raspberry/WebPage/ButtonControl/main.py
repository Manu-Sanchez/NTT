from flask import Flask, render_template, request
import RPi.GPIO as gpio
import os

app = Flask(__name__)

def gpio_start():
	global LED_PIN
	LED_PIN = 7

	gpio.setmode(gpio.BOARD)
	gpio.setup(LED_PIN, gpio.OUT)


@app.route("/", methods=["GET", "POST"])
def action():
	if request.method == "POST":
		if request.form.get("action1") == "ON":
			gpio.output(LED_PIN, gpio.HIGH)
	
		if request.form.get("action2") == "OFF":
			gpio.output(LED_PIN, gpio.LOW)

	return render_template("index.html")

gpio_start()
app.run(host = "0.0.0.0", port=5000, debug=True)

from flask import Flask, render_template
from flask import Flask
from flask import request
import subprocess
import lightTools

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('main.html')
@app.route('/tools')
def tools():
	return render_template('tools.html')
@app.route('/run')
def run():
	subprocess.call(['sudo /home/pi/rpi_ws281x/test'], shell=True)
	return 'success'
@app.route('/rainbow')
def rainbow():
	lightTools.rainbow()
@app.route('/allOn')
def turnAllLightsOn():
	lightTools.turnOnAll()
	return 'success'
@app.route('/allOff')
def turnAllLightsOff():
	lightTools.turnOffAll()
	return 'success'
@app.route('/blink')
def blink():
	lightTools.blink()
	return 'success'
@app.route('/message/<message>')
def displayMessage(message):
	lightTools.sendMessage(message)
	return message
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=80)
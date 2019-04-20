from flask import Flask, render_template, request, jsonify
import os
from sys import stdout
from os.path import stat
from time import sleep
from raspberry import RaspberryThread
from sensor_function import listen


app = Flask(__name__)

device_status = "RUNNING"
monitoring_status = "STOPPED"


@app.route('/')
def dashboard():
	return renderdashboard();

@app.route('/webservices')
def webservices():
	return render_template("webservices.html")

@app.route('/help')
def help():
	return render_template("help.html")

#========== WEB SERVICES ==============
@app.route('/v1/startmonitoring', methods=['GET'])
def startmonitoring():
	global monitoring_status
	print("startmonitoring() - monitoring_status: ", monitoring_status)
	if not monitoring_thread.isAlive():
		monitoring_thread.start()
	
	monitoring_thread.resume()
	
	monitoring_status = "STARTED"
	print("monitoring_status: ", monitoring_status)
	return renderdashboard()

@app.route('/v1/stopmonitoring', methods=['GET'])
def stopmonitoring():
	global monitoring_status
	print("stopmonitoring()")
	if not monitoring_thread.isAlive():
		monitoring_thread.stop()
	
	monitoring_status = "STOPPED"
	print("monitoring_status: ", monitoring_status)
	return renderdashboard()

@app.route('/v1/poweroff', methods=['GET'])
def poweroff():
	# cmdCommand = "shutdown -h now"
	# process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
	# return jsonify(status="SHUTTING_DOWN", process_pid=process.pid, process_return_code=process.returncode)
	os.system("sudo shutdown now -h")
	device_status = "SHUTTING_DOWN"
	return status()

@app.route('/v1/status', methods=['GET'])
def status():
	
	return jsonify(device_status=device_status
				, monitoring_status=monitoring_status
				)

def renderdashboard():
	#TODO: check if monitoring is started or not
	## and change label definition
	global monitoring_status
	print("renderdashboard() - monitoring_status: ", monitoring_status)
	if monitoring_status == "STOPPED":
		monitoring_button_label='Start Monitoring'
	else:
		monitoring_button_label='Stop Monitoring'
	
	return render_template("dashboard.html",
						monitoring_status=monitoring_status, 
						monitoring_button_label=monitoring_button_label
						)


if __name__ == '__main__':
	# Create threads
	monitoring_thread = RaspberryThread(function = listen)
	
	# collect threads
	threads = [
		monitoring_thread
	] 
	
	app.run(debug=True, host='0.0.0.0', port=80, threaded=True)


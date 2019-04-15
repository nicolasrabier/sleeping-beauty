from flask import Flask, render_template, request, jsonify
import os
from sys import stdout

app = Flask(__name__)

@app.route('/')
def dashboard():
	#TODO: check if monitoring is started or not
	start_stop_monitoring_button_label='Start Monitoring'
	
	return render_template("dashboard.html", start_stop_monitoring_button_label=start_stop_monitoring_button_label)

@app.route('/webservices')
def webservices():
	return render_template("webservices.html")

@app.route('/help')
def help():
	return render_template("help.html")

@app.route('/v1/startmonitoring', methods=['GET'])
def startmonitoring():
	
	return jsonify(status="MONITORING STARTED")

@app.route('/v1/stopmonitoring', methods=['GET'])
def stopmonitoring():

	return jsonify(status="MONITORING STOPPED")

@app.route('/v1/poweroff', methods=['GET'])
def poweroff():
	# cmdCommand = "shutdown -h now"
	# process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
	# return jsonify(status="SHUTTING_DOWN", process_pid=process.pid, process_return_code=process.returncode)
	os.system("sudo shutdown now -h")
	return jsonify(status="SHUTTING_DOWN")

@app.route('/v1/status', methods=['GET'])
def status():
	return jsonify(status='RUNNING')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


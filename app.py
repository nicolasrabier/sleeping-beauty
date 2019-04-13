from flask import Flask, render_template, request, jsonify
import subprocess
from sys import stdout

app = Flask(__name__)

@app.route('/')
def dashboard():
	return render_template("dashboard.html")

@app.route('/webservices')
def webservices():
	return render_template("webservices.html")

@app.route('/help')
def help():
	return render_template("help.html")

@app.route('/v1/switchoff', methods=['GET'])
def switchoff():
	cmdCommand = "shutdown -h now"
	process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
	return jsonify(status="SHUTTING_DOWN", process_pid=process.pid)

@app.route('/v1/status', methods=['GET'])
def status():
	return jsonify(status='RUNNING')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


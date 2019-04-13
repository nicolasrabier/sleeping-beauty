from flask import Flask, render_template, request, jsonify

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

@app.route('/v1/status', methods=['GET'])
def status():
	return jsonify(status=OK)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


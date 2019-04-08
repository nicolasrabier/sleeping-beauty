from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("dashboard.html")

@app.route('/webservices')
def webservices():
	return render_template("webservices.html")

@app.route('/help')
def webservices():
	return render_template("help.html")

@app.route('/v1/status')
def status():
	return '{"status":"OK"}';

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


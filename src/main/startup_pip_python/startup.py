from flask import Flask
app = Flask(__name__)

@app.route("/startup")
def startup():
    return "Startup!"

@app.route("/startupv2")
def startup():
    return "Startup Version 2!"

if __name__ == '__main__':
	app.run (host='0.0.0.0') 

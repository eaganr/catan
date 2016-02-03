from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
	f = {}
	f["yo"] = 10
	f["bob"] = 20

	resp = Response(response=f, status=200, mimetype="application/json")
	return(resp)

if __name__ == "__main__":
	app.run()

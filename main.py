from flask import Flask, Response
import json
import pymysql
from dbinfo import IP, USER, PASSWORD, DB

app = Flask(__name__)

@app.route("/")
def hello():
	#mysql
	conn = pymysql.connect(host=IP, user=USER, password=PASSWORD, db=DB)
	cur = conn.cursor();
	sql = "SELECT * from resources;"
	cur.execute(sql)
	result = cur.fetchall()
	print(result)


	resp = Response(response=json.dumps(result), status=200, mimetype="application/json")
	return resp

if __name__ == "__main__":
	app.run()

from API_Request import getStation
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/WebMap")
def hello_world():
    return render_template("index.html", bitch_var="Hello World")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)



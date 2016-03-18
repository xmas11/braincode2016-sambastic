from flask import Flask
from flask import render_template
from test import Query

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/mvp")
def mvp():
    q = Query()
    offers = q.query("thinkpad x230")["offers"]
    return render_template("mvp.html", offers=offers)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import render_template
from test import Query
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    return "Sambastic Alle"

@app.route("/mvp/<req>")
def mvp(req):
    q = Query()
    offers = q.query(req)["offers"]
    prices = []
    for offer in offers:
        prices.append(offer['prices']['buyNow'])
    plt.hist(prices)
    plt.savefig('static/hist.png')
    return render_template("mvp.html", offers=offers)

if __name__ == '__main__':
    app.run(debug=True)

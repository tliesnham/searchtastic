import searchtastic

from searchtastic import Searchtastic

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    results = Searchtastic.search(keyword)
    return results

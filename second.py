from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    names=["mari","sergi","lika","giga","nuca","ziza"]
    return render_template("index.html", list_of_names=names)


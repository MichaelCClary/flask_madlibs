from flask import Flask, request, render_template
from stories import Story, story


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/story")
def create_story():

    text = story.generate(request.args)

    return render_template("story.html", text=text)

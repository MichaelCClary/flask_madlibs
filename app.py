from flask import Flask, request, render_template
from stories import Story, story


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/story")
def create_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    ans = {"place": place, "noun": noun, "verb": verb,
           "adjective": adjective, "plural_noun": plural_noun}

    text = story.generate(ans)

    return render_template("story.html", text=text)

from flask import Flask, render_template
from aesop import Aesop

app = Flask(__name__)

new_story = Aesop("original_stories.txt")
new_story.make_dict()

@app.route('/')
def home():
    with open("static/welcome.html") as f:
        return f.read()


@app.route('/story')
def story():
    fable = new_story.gen_story()
    return render_template('new_story.html', fable=fable)

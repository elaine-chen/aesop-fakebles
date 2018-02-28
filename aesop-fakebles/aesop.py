from parser import Parser
import gen
from flask import Flask, render_template
import grab_titles


app = Flask(__name__)


class Aesop:

    def __init__(self, source):
        self.lines = grab_titles.grab(source)
        self.title_dict = {}
        self.text_dict = {}
        self.morals_dict = {}

    def dict_generator(self, source, k):
        to_parse = Parser(source, k)
        return to_parse.parse()

    def make_dict(self):
        t = grab_titles.grab_t(self.lines)
        txt = grab_titles.grab_txt(self.lines)
        m = grab_titles.grab_m(self.lines)
        self.title_dict = self.dict_generator(t, 2)
        self.text_dict = self.dict_generator(txt, 2)
        self.morals_dict = self.dict_generator(m, 1)

    def gen_story(self):
        body = gen.gen_text(self.text_dict, 500, True, len(self.text_dict))
        title = gen.gen_text(self.title_dict, 3, False, len(self.title_dict))
        moral = gen.gen_text(self.morals_dict, 10, True, len(self.morals_dict))
        return Fable(title, body, moral)

class Fable:

    def __init__(self, title, body, moral):
        self.title = title
        self.body = body
        self.moral = moral

    def __str__(self):
        return self.title + "\n\n\t" + self.body + "\n\n\t" + self.moral

@app.route('/')
def home():
    with open("static/welcome.html") as f:
        return f.read()

@app.route('/story')
def story():
    new_story = Aesop("original_stories.txt")
    new_story.make_dict()
    fable = new_story.gen_story()
    return render_template('new_story.html', fable=fable)

    # response = app.make_response(to_display)
    # response.headers["content-type"] = "text/plain"
    # return response

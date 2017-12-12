from parser import Parser
import gen
from flask import Flask
import grab_titles

def gen_dict(source, k):
    to_parse = Parser(source, k)
    return to_parse.parse()

app = Flask(__name__)

lines = grab_titles.grab("11339-8.txt")

t = grab_titles.grab_t(lines)
title_dict = gen_dict(t, 2)
title_dict_len = len(title_dict)

txt = grab_titles.grab_txt(lines)
text_dict = gen_dict(txt, 2)
text_dict_len = len(text_dict)

m = grab_titles.grab_m(lines)
morals_dict = gen_dict(m, 1)
morals_dict_len = len(morals_dict)

def gen_story():
    body =  gen.gen_text(text_dict, 500, True, text_dict_len)
    title = gen.gen_text(title_dict, 10, False, title_dict_len)
    moral = gen.gen_text(morals_dict, 10, True, morals_dict_len)
    return title + "\n\n\t" + body + "\n\n\t" + moral


@app.route('/')
def story():
    response = app.make_response(gen_story())
    response.headers["content-type"] = "text/plain"
    return response

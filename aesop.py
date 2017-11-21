from parser import Parser
import gen
from flask import Flask
import grab_titles

def gen_dict(source, k):
    to_parse = Parser(source, k)
    print "DICTONARY HAS BEEN GENERATED"
    return to_parse.parse()

app = Flask(__name__)

lines = grab_titles.grab("11339-8.txt")

# story_dict = gen_dict("11339-8.txt")
# story_dict_len = len(story_dict)
# grab_titles.get_titles()
# grab_titles.get_morals()
t = grab_titles.grab_t(lines)
title_dict = gen_dict(t, 2)
title_dict_len = len(title_dict)

txt = grab_titles.grab_txt(lines)
text_dict = gen_dict(txt, 2)
text_dict_len = len(text_dict)

m = grab_titles.grab_m(lines)
morals_dict = gen_dict(m, 1)
print morals_dict
morals_dict_len = len(morals_dict)




@app.route('/')
def story():
    body =  gen.gen_text(text_dict, 500, True, text_dict_len)
    title = gen.gen_text(title_dict, 10, False, title_dict_len) + '\n'
    moral = '\t' + gen.gen_text(morals_dict, 10, True, morals_dict_len)
    return moral

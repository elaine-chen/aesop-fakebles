from flask import Flask
from Parser import parser
import parser_text
import gen

app = Flask(__name__)

@app.route('/')
def gen_story():
    return parser_text.main("fab.mb.txt")

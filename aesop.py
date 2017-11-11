from parser import Parser
import gen
from flask import Flask

def main(source):
    to_parse = Parser(source, 2)
    freq = to_parse.parse()
    return gen.gen_text(freq, 500)

app = Flask(__name__)

@app.route('/')
def story():
    return main("fab.mb.txt")

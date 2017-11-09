from parser import Parser
import gen

def main(source):
    to_parse = Parser(source, 2)
    freq = to_parse.parse()
    return gen.gen_text(freq, 500)

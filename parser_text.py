from parser import Parser
import gen

def main():
    to_parse = Parser("fab.mb.txt", 2)
    freq = to_parse.parse()
    return gen.gen_text(freq, 300)


main()

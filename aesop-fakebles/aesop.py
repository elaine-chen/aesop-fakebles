from parser import Parser
import gen
import grab_titles

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
        fable= Fable(title, body, moral)
        fable.body = unicode(body, "latin-1")
        return fable

class Fable:

    def __init__(self, title, body, moral):
        self.title = title
        self.body = body
        self.moral = moral

    def __str__(self):
        return self.title + "\n\n\t" + self.body + "\n\n\t" + self.moral

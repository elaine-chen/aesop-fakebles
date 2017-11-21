class Parser:

    def __init__(self, text, k_value):
        self.text = text
        self.k_value = k_value
        self.freq_map = {}

    """using a nested dictionary instead,
       dict = {word:{sub_word: freq, subword_freq: freq, etc}}"""

    """in making the freq dictionary for the story, words in all caps (titles)
    are skipped"""
    def parse(self):
        to_chunk = []
        for line in self.text:
            to_chunk += line.split()
        chunks = [to_chunk[x:x+(self.k_value+1)] for x in xrange(0, len(to_chunk))]
        for chunk in chunks:
            self.find_freq(chunk)
        return self.freq_map

    def find_freq(self, phrase):
        if len(phrase) < self.k_value +1:
            return
        key_phrase = tuple(phrase[:self.k_value])
        sub_word = phrase[-1]
        if key_phrase in self.freq_map:
            count = self.freq_map[key_phrase].get(sub_word, 0)
            self.freq_map[key_phrase][sub_word] = count + 1
        else:
            self.freq_map[key_phrase] = {sub_word: 1}

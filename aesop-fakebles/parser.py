class Parser:

    def __init__(self, text, k_value):
        self.text = text
        self.k_value = k_value
        self.freq_map = {}
        self.to_chunk = []

    def parse(self):
        for line in self.text:
            self.to_chunk += line.split()
        chunks = [self.to_chunk[x:x+(self.k_value+1)] for x in xrange(0, len(self.to_chunk))]
        for chunk in chunks:
            self.find_freq(chunk)
        return self.freq_map

    def find_freq(self, phrase):
        """if the phrase is smaller than the length of k (when we are at the
        end of the source), the text loops around """
        if len(phrase) < self.k_value +1:
            phrase += self.to_chunk[1:self.k_value -len(phrase)]
        key_phrase = tuple(phrase[:self.k_value])
        sub_word = phrase[-1]
        if key_phrase in self.freq_map:
            count = self.freq_map[key_phrase].get(sub_word, 0)
            self.freq_map[key_phrase][sub_word] = count + 1
        else:
            self.freq_map[key_phrase] = {sub_word: 1}

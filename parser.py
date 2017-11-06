class Parser:

    def __init__(self, text, k_value):
        self.text = text
        self.k_value = k_value
        self.freqMap = {}

    """using a nested dictionary instead, dict = {word:{sub_word: freq, subword_freq: freq, etc}}"""

    def parse(self):
        #f = file(self.text).read()
        with open(self.text, "r") as f:
            t = f.read().split()

        chunks = [t[x:x+(self.k_value+1)] for x in xrange(0, len(t))]
        for chunk in chunks:
            # print chunk
            self.find_freq(chunk)
        return self.freqMap



    def find_freq(self, phrase):
        if len(phrase) < self.k_value +1:
            return
        key_phrase = tuple(phrase[:self.k_value])
        sub_word = phrase[self.k_value]
        if key_phrase in self.freqMap:
            count = self.freqMap[key_phrase].get(sub_word)
            if count != None:
                self.freqMap[key_phrase][sub_word] += 1
            else:
                self.freqMap[key_phrase][sub_word] = 1
        else:
            self.freqMap[key_phrase] = {sub_word: 1}

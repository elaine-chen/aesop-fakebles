from random import randint
import numpy as np

body = []

def gen_text(freqMap, length):
    l = len(freqMap)
    n = randint(0,l)
    cur = freqMap.keys()[randint(0,l)]
    # print "current word ", cur
    body.append("   ")
    start_sen = True
    body.append(cur[0][0].capitalize() + cur[0][1:])
    body.append(cur[1])
    while length > 0:
        for each in cur:
            if start_sen == True:
                each = each[0].capitalize() + each[1:]
                start_sen = False
        #***if current ends with period, make start_sen = True
            if each[-1] == ".":
                start_sen = True
            # body.append(''.join(each))
        # print "current word has subwords ", freqMap[cur]
        # print "removing the first word ", cur, cur[1:]
        next_word = (get_random(freqMap[cur]),)
        body.append(''.join(next_word))
        cur = cur[1:] + (next_word)
        print "NEW cur is ", cur
        length -= 1
    # print body
    print " ".join(body)


def get_random(subwords):
    prob_dist = []
    prob_words = []
    freq_sum = sum(subwords.values())
    for item in subwords:
        # print "the item ", item
        prob_dist.append((subwords[item]+0.0)/freq_sum)
        prob_words.append(item)
        # print "Potential words ", prob_words
    return np.random.choice(prob_words, p = prob_dist)

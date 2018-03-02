from random import randint
import numpy as np


def gen_text(freq_map, length, is_story, map_len):

    """the boolean not_at_end is used to prevent the while-loop from
    ending when the last word generated is not at the end of a sentence even
    though the initial length has been fulfilled. It serves a similar function
    in latter part of the function where titles are being generated. It is
    used to make the ends of paragraphs and sentenses look more natural
    """
    text = ""
    body = []
    cur = freq_map.keys()[randint(0, map_len)]
    body.append(cur[0][0].capitalize() + cur[0][1:])
    for word in cur[1:]:
        body.append(word)
    not_at_end = True
    while length > 0 or not_at_end is True:
        print "CUR IS ", cur
        next_word = get_random(freq_map[cur])
        print "next word is ", next_word
        body.append(next_word)
        cur = cur[1:] + (next_word,)
        length -= 1
        if length <= 0:
            if is_story is True:
                if body[-1][-1] in [".", "?", "!"]:
                    not_at_end = False
                    text = " ".join(body)
                else:
                    continue
            if body[-1] != "THE" and body[-1] != "AND" and body[-1] != "HIS":
                not_at_end = False
                if body[0] == "AND":
                    body = body[1:]
                text = " ".join(body)
                if text[-1] == ",":
                    text = text[:-1]
    return text


def get_random(subwords):
    prob_dist = []
    prob_words = []
    freq_sum = sum(subwords.values())
    for item in subwords:
        prob_dist.append((subwords[item]+0.0)/freq_sum)
        prob_words.append(item)
    return np.random.choice(prob_words, p = prob_dist)

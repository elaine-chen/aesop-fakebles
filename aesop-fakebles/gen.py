from random import randint
import numpy as np

"""in terms of generating titles i would love to add a comma at the end of the
    word that occurs befor every 'the' ?? """

def gen_text(freq_map, length, is_story, map_len):
    text = ""
    l_dup = length
    body = []
    cur = freq_map.keys()[randint(0,map_len)]
    print "current word ", cur
    body.append(cur[0][0].capitalize() + cur[0][1:])
    for word in cur[1:]:
        body.append(word)
    print body
    not_at_end = True
    while length > 0 or not_at_end == True:
        next_word = get_random(freq_map[cur])
        body.append(next_word)
        cur = cur[1:] + (next_word,)
        length -= 1
        if length <= 0:
            if is_story == True:
                if body[-1][-1] in [".", "?", "!"]:
                    not_at_end = False
                    body.insert(0, "\t")
                    text = " ".join(body)
                    break
                else:
                    continue
            else:
                if body[-1] != "THE" and body[-1] != "AND" and body[-1] != "HIS":
                    not_at_end = False
                    if body[0] == "AND":
                        body = body[1:]
                    text = " ".join(body)
                    print body
                    if text[-1] == ",":
                        text = text[:-1]
                    break
                else:
                    continue
        else:
            continue
    return text


def get_random(subwords):
    prob_dist = []
    prob_words = []
    freq_sum = sum(subwords.values())
    for item in subwords:
        prob_dist.append((subwords[item]+0.0)/freq_sum)
        prob_words.append(item)
    return np.random.choice(prob_words, p = prob_dist)

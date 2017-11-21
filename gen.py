from random import randint
import numpy as np

"""in terms of generating titles i would love to add a comma at the end of the
    word that occurs befor every 'the' ?? """

def gen_text(freq_map, length, is_story, map_len):
    l_dup = length
    body = []
    cur = freq_map.keys()[randint(0,map_len)]
    # print "current word ", cur
    body.append("   ")
    body.append(cur[0][0].capitalize() + cur[0][1:])
    body.append(cur[1])
    while length > 0:
        next_word = get_random(freq_map[cur])
        body.append(next_word)
        cur = cur[1:] + (next_word,)
        length -= 1
    if is_story:
        story = " ".join(body)
        if story[-1] in [".", "?", "!"]:
            return story
        else:
            last_word_ind = max(story.rfind("."), story.rfind("!"), story.rfind("?"))
            return story[:last_word_ind+1]
    else:
        if body[-1] != "THE" and body[-1] != "AND":
            title = " ".join(body)
        else:
            for i in reversed(xrange(l_dup+1)):
                if body[i] != "THE" and body[i] != "AND":
                    body = body[:i+1]
                    break
                else:
                    continue
            title = " ".join(body)
        if title[-1] == ",":
            title = title[:-1]
        return title


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

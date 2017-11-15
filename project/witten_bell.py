from config import *
from cond_prob import *

def witten_bell(prev_words, cur_word):
    if prev_words == []:
        return cond_prob(prev_words,cur_word)
   
    if len(prev_words) == 1:
        num = count_distinct_uni[prev_words[0]]
        den = num + unigram[prev_words[0]] 
    else:
        num = count_distinct_bi[prev_words[0] + ' ' + prev_words[1]]
        den = num + bigram[prev_words[0] + ' ' + prev_words[1]]

    if den == 0:
        return 0
            
    const = 1 - float(num)/den
    ans = const*cond_prob(prev_words,cur_word)+(1-const)*witten_bell(prev_words[1:],cur_word)
    return ans

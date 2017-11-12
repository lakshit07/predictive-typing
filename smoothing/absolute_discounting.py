from cond_prob import *
from config import *
from math import *

def absolute_discounting(prev_words, cur_word):
    D = float(count_trigram[1])/( count_trigram[1] + 2*count_trigram[2] )
    
    if prev_words == []:
        return max(unigram[cur_word] - D, 0)/config.total_unigrams

    if len(prev_words) == 1:
        den = unigram[prev_words[0]]
        if den == 0:
            return 0
        const = (D/unigram[prev_words[0]]) * count_distinct_uni[prev_words[0]]
        num = max(bigram[prev_words[0] + ' ' + cur_word] - D, 0)
    else:
        den = bigram[prev_words[0] + ' ' + prev_words[1]]
        if den == 0:
            return 0
        const = (D / bigram[prev_words[0] + ' ' + prev_words[1]]) * count_distinct_bi[prev_words[0] + ' ' + prev_words[1]]
        num = max(trigram[prev_words[0] + ' ' + prev_words[1] + ' ' + cur_word] - D, 0)

    ans = const * absolute_discounting(prev_words[1:], cur_word)
    if den != 0:
        ans += float(num)/den
    return ans

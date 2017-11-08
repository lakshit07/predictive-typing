from cond_prob import *

def jelinek_mercer(prev_words,cur_word):
	const = 0.4
	if prev_words == []:
		return cond_prob(prev_words,cur_word)
	ans = const*cond_prob(prev_words,cur_word)+(1-const)*jelinek_mercer(prev_words[1:],cur_word)
	return ans
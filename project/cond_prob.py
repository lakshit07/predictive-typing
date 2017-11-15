import config
from config import *

def cond_prob(prev_words,cur_word):
	full_word = ''
	partial_word = ''
	if prev_words == []:
		full_word = cur_word
	else:
		for word in prev_words:
			partial_word += (word+' ')
		partial_word = partial_word[:-1]
		full_word = partial_word + ' ' + cur_word
	order = len(prev_words)+1
	if order==1:
		return float(unigram[full_word])/config.total_unigrams
	elif order==2:
		num = bigram[full_word]
		denom = unigram[partial_word]
		if num == 0 and denom == 0:
			return 0
		return float(num)/denom
	else:
		num = trigram[full_word]
		denom = bigram[partial_word]
		if num == 0 and denom == 0:
			return 0
		return float(num)/denom
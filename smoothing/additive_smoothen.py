from config import *

def additive_smoothen(prev_words,cur_word):
	full_word = ''
	partial_word = ''
	for word in prev_words:
		partial_word += (word+' ')
	partial_word = partial_word[:-1]
	full_word = partial_word + ' ' + cur_word
	num = trigram[full_word]
	denom = bigram[partial_word]
	delta = 1
	num += delta
	denom += (delta*voc_size)
	return float(num)/denom
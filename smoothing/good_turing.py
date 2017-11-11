from config import *

def good_turing(prev_words,cur_word):
	full_word = ''
	for word in prev_words:
		full_word += (word+' ')
	full_word += cur_word
	r = trigram[full_word]
	if r==0:
		return 0
	nr = count_trigram[r]
	nr1 = count_trigram[r+1]
	new_r = (float(r+1)*nr1)/nr
	N = 0
	for (key,value) in count_trigram.items():
		N += (key*value)
	return float(new_r)/N

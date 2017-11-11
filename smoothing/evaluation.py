import re
from absolute_discounting import *
from additive_smoothen import *
from good_turing import *
from jelinek_mercer import *
from witten_bell import *
from math import log

def evaluation(testfile,method):
	f = open(testfile,'r')
	total_words = 0
	cross_entropy = 0.0
	for sentence in f:
		split_sentence = re.split(regexPattern,sentence)
		prev_word = prev2_word = ''
		for word in split_sentence:
			if word=='':
				continue
			total_words += 1
			if prev_word == '':
				cross_entropy += log(cond_prob([],word),2)
			elif prev2_word == '':
				cross_entropy += log(cond_prob([prev_word],word),2)
			elif method == 'additive':
				cross_entropy += log(additive_smoothen([prev2_word,prev_word],word),2)
			elif method == 'turing':
				val1 = good_turing([prev2_word,prev_word],word)
				if val1 != 0: 
					cross_entropy += log(val1,2)
				else:
					val2 = cond_prob([prev2_word,prev_word],word)
					if val2 != 0:
						cross_entropy += log(val2,2)
					else:
						val3 = cond_prob([prev_word],word)
						if val3 != 0:
							cross_entropy += log(val3,2)
						else:
							cross_entropy += log(cond_prob([],word),2)

			elif method == 'jelinek mercer':
				cross_entropy += log(jelinek_mercer([prev2_word,prev_word],word),2)
			elif method == 'witten bell':
				cross_entropy += log(witten_bell([prev2_word,prev_word],word),2)
			elif method == 'absolute discounting':
				cross_entropy += log(absolute_discounting([prev2_word,prev_word],word),2)

			prev2_word = prev_word
			prev_word = word

	cross_entropy /= (-total_words)
	perplexity = 2.0 ** cross_entropy
	return (perplexity,cross_entropy)

	f.close()
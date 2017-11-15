import re,os,json
from absolute_discounting import *
from additive_smoothen import *
from good_turing import *
from jelinek_mercer import *
from witten_bell import *
from math import log

def evaluation(testfolder,method):
	default_p = 1.0/config.total_unigrams
	perp = []
	c_entropy = []

	for testfile in os.listdir(testfolder):
		f = open(testfolder+'/'+testfile,'r')
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
					p = cond_prob([],word)
					if p==0:
						p = default_p
					cross_entropy += log(p,2)
				elif prev2_word == '':
					p = cond_prob([prev_word],word)
					if p==0:
						p = default_p
					cross_entropy += log(p,2)
				elif method == 'additive':
					p = additive_smoothen([prev2_word,prev_word],word)
					if p==0:
						p = default_p
					cross_entropy += log(p,2)
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
								p = cond_prob([],word)
								if p==0:
									p = default_p
								cross_entropy += log(p,2)

				elif method == 'jelinek mercer':
					p = jelinek_mercer([prev2_word,prev_word],word)
					if p==0:
						p = default_p
					cross_entropy += log(p,2)
				elif method == 'witten bell':
					p = witten_bell([prev2_word,prev_word],word)
					if p==0:
						p = default_p
					cross_entropy += log(p,2)
				elif method == 'absolute discounting':
					p = absolute_discounting([prev2_word,prev_word],word)
					if p==0:
						p = default_p
					cross_entropy += log(p,2)

				prev2_word = prev_word
				prev_word = word

		cross_entropy /= (-total_words)
		perplexity = 2.0 ** cross_entropy
		perp.append(perplexity)
		c_entropy.append(cross_entropy)
		f.close()

	return (perp,c_entropy)


def evaluation_all(foldername):
	(perp1,c_entropy1) = evaluation(foldername,'additive')
	(perp2,c_entropy2) = evaluation(foldername,'turing')
	(perp3,c_entropy3) = evaluation(foldername,'jelinek mercer')
	(perp4,c_entropy4) = evaluation(foldername,'witten bell')
	(perp5,c_entropy5) = evaluation(foldername,'absolute discounting')
	c_entropy_all = [c_entropy1,c_entropy2,c_entropy3,c_entropy4,c_entropy5]
	perp_all = [perp1,perp2,perp3,perp4,perp5]
	return (c_entropy_all,perp_all) 

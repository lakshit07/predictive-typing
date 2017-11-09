import os
import config
from config import * 

def get_counts(foldername):
	for fn in os.listdir(foldername):
		filename = foldername+"/"+fn
		f = open(filename,'r')
		print "Processing file ",filename
		for sentence in f:
			split_sentence = re.split(regexPattern,sentence)
			prev_word = prev2_word = ''
			for word in split_sentence:
				if word=='':
					continue
				unigram[word] += 1
				config.total_unigrams += 1
				if prev_word != '':
					bigram[prev_word+' '+word] += 1
					if bigram[prev_word + ' ' + word] == 1:
						count_distinct_uni[prev_word] += 1
				if prev2_word != '':
					trigram[prev2_word+' '+prev_word+' '+word] += 1
					if trigram[prev2_word + ' ' + prev_word + ' ' + word] == 1:
						count_distinct_bi[prev2_word + ' ' + prev_word] += 1
				prev2_word = prev_word
				prev_word = word
		f.close()

	for (key,value) in unigram.iteritems():
		count_unigram[value] += 1
	for (key,value) in bigram.iteritems():
		count_bigram[value] += 1
	for (key,value) in trigram.iteritems():
		count_trigram[value] += 1
	config.voc_size = len(unigram)

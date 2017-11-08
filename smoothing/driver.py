from dictionary import *
from additive_smoothen import *
from good_turing import *
from jelinek_mercer import *
from cond_prob import *
import config
import Queue,time
from Queue import PriorityQueue

def predict(prev_words,method):
	no_of_words = 10
	pq = Queue.PriorityQueue()
	for (word,value) in unigram.iteritems():
		prob = 0
		if method=='additive':
			prob = additive_smoothen(prev_words,word)
		elif method=='turing':
			prob = good_turing(prev_words,word)
		elif method=='jelinek mercer':
			prob = jelinek_mercer(prev_words,word)

		pq.put((-prob,word))

	word_lst = []
	for i in range(no_of_words):
		(neg_prob,word) = pq.get()
		word_lst.append((word,-neg_prob))
	return word_lst

def get_prediction(sentence,method):
	split_sentence = re.split(regexPattern,sentence)
	prev_word = prev2_word = ''
	for word in split_sentence:
		if word=='':
			continue
		if prev_word != '' and prev2_word != '':
			predictions = predict([prev2_word,prev_word],method)
			print "Prediction for word ",word," is ",predictions
		prev2_word = prev_word
		prev_word = word

start_time=time.time()
get_counts("./data")
print "Obtaining counts: ",time.time()-start_time," seconds"
print "Voc size: ",config.voc_size
sentence = "he has a phone pole sticking in his chest i think we dont need an autopsy"
sentence = "these are the experiences that write our story and shape our lives" 
print 'Additive smoothing'
get_prediction(sentence,'additive')
print ''
print 'Good Turing'
get_prediction(sentence,'turing')
print ''
print 'Jelinek-Mercer'
get_prediction(sentence,'jelinek mercer')
#print cond_prob(["at","a"],"baptist")
#print count_unigram
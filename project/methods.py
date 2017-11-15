from dictionary import *
from additive_smoothen import *
from good_turing import *
from jelinek_mercer import *
from witten_bell import *
from cond_prob import *
from absolute_discounting import *
import config
import time
import heapq
import json


def predict(prev_words,method):
	no_of_words = 10
	pq = []
	for (word,value) in unigram.items():
		prob = 0
		if method=='additive':
			prob = additive_smoothen(prev_words,word)
		elif method=='turing':
			prob = good_turing(prev_words,word)
		elif method=='jelinek mercer':
			prob = jelinek_mercer(prev_words,word)
		elif method=='witten bell':
			prob = witten_bell(prev_words , word)
		elif method == 'absolute discounting':
			prob = absolute_discounting(prev_words, word)	
		else:
			pass
		heapq.heappush(pq, (-prob,word))

	word_lst = []
	for i in range(no_of_words):
		(neg_prob,word) = heapq.heappop(pq)
		word_lst.append((word,-neg_prob))
	return word_lst

def get_prediction(sentence,method):
	split_sentence = re.split(regexPattern,sentence)
	prev_word = prev2_word = ''
	ans = ""
	for word in split_sentence:
		if word=='':
			continue
		if prev_word != '' and prev2_word != '':
			predictions = predict([prev2_word,prev_word],method)
			ans += "Prediction for word " + str(word) + " is " + str(predictions) + "\n"
		prev2_word = prev_word
		prev_word = word
	return ans	
	

def get_prediction_json(sentence,method):
	no_of_words = 10
	pq = []
	split_sentence = re.split(regexPattern,sentence)
	prev_word = prev2_word = ''
	for word in split_sentence:
		if word=='':
			continue
		prev2_word = prev_word
		prev_word = word
	prev_words = [prev2_word,prev_word]

	for (word,value) in unigram.items():
		prob = 0
		if method=='additive':
			prob = additive_smoothen(prev_words,word)
		elif method=='turing':
			prob = good_turing(prev_words,word)
		elif method=='jelinekmercer':
			prob = jelinek_mercer(prev_words,word)
		elif method=='wittenbell':
			prob = witten_bell(prev_words , word)
		elif method == 'absolutediscounting':
			prob = absolute_discounting(prev_words, word)	
		else:
			pass
		heapq.heappush(pq, (-prob,word))

	data={"words":[],"predictions":[]}

	for i in range(no_of_words):
		(neg_prob,word) = heapq.heappop(pq)
		data["words"].append(word)
		data["predictions"].append(-neg_prob)

	return json.dumps(data)	


def compute():
	if len(unigram) == 0:
		start_time=time.time()
		get_counts("../data")
		print("Obtaining counts: ",time.time()-start_time," seconds")
		print("Voc size: ",config.voc_size)
		comp = True
		return "done"


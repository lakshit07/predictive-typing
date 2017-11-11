from methods import *
from evaluation import *
import os

def main():
	print(compute('turing'))
	sentence = "these are the experiences that write our story and shape our lives"
	print (get_prediction_json(sentence,'additive'))
	print (get_prediction_json(sentence,'turing'))
	print (get_prediction_json(sentence,'jelinek mercer'))
	print (get_prediction_json(sentence,'witten bell'))
	print (get_prediction_json(sentence,'absolute discounting'))

	# print(compute('turing'))
	# testfile = './test/test.txt'
	# print ('Additive smoothing')
	# (perplexity,cross_entropy) = evaluation(testfile,'additive')
	# print ('Perplexity is ',perplexity,' and cross entropy is ',cross_entropy)

	# print ('Good Turing')
	# (perplexity,cross_entropy) = evaluation(testfile,'turing')
	# print ('Perplexity is ',perplexity,' and cross entropy is ',cross_entropy)

	# print ('Jelinek-mercer')
	# (perplexity,cross_entropy) = evaluation(testfile,'jelinek mercer')
	# print ('Perplexity is ',perplexity,' and cross entropy is ',cross_entropy)

	# print ('Witten Bell')
	# (perplexity,cross_entropy) = evaluation(testfile,'witten bell')
	# print ('Perplexity is ',perplexity,' and cross entropy is ',cross_entropy)

	# print ('Absolute Discounting')
	# (perplexity,cross_entropy) = evaluation(testfile,'absolute discounting')
	# print ('Perplexity is ',perplexity,' and cross entropy is ',cross_entropy)


if __name__ == "__main__":
    main()	

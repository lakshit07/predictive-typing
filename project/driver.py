from methods import *
import json
from evaluation import *
from endpoints import Controller, CorsMixin
import os
import sys
from resource import *

class Default(Controller, CorsMixin):
    def GET(self):
   		compute()
   		data = {"one": 1, "two": 2}
		json_data = json.dumps(data)
		return json_data

class Predict(Controller, CorsMixin):
    def GET(self):
        return "Enter the parameters"
    
    def POST(self, **kwargs):
    	sentence = kwargs['sentence']
    	sentence = sentence.replace(",", " ")
    	print(sentence)
    	print(kwargs['method'])
    	return get_prediction_json(sentence, kwargs['method'])

class Evaluate(Controller, CorsMixin):
    def GET(self):
        d = {}
        l = evaluation_all("test")
        d['crossentropy'] = l[0]
        d['perplexity'] = l[1]
        json_data = json.dumps(d)
        return json_data

class Semantic(Controller, CorsMixin):
    def GET(self):
        load()
        data = {"one": 1, "two": 2}
        json_data = json.dumps(data)
        return json_data

    def POST(self, **kwargs):
        sentence1 = kwargs['sentence1']
        sentence2 = kwargs['sentence2']
        print sentence1
        print sentence2
        a = calc(sentence1, sentence2)
        d = {}
        if a < 0.5:
            d['comment'] = "Not Duplicate : "
        else:
            d['comment'] = "Duplicate : "    
        d['score'] = a
        jsob = json.dumps(d)
        print "json object = " , jsob
        return jsob




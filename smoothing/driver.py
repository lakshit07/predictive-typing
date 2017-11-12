from methods import *
import json
from evaluation import *
from endpoints import Controller, CorsMixin
import os

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


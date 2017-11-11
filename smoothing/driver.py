from methods import *
from endpoints import Controller
import os

class Default(Controller):
    def GET(self):
    	compute()
        return "Welcome to Typing Predictor"

class Predict(Controller):
    def GET(self):
        return "Enter the parameters"
    
    def POST(self, **kwargs):
        if kwargs['method'] == "additive":
            return get_prediction(kwargs['sentence'] , 'additive')
        elif kwargs['method'] == "turing":
            return get_prediction(kwargs['sentence'], 'turing')
        elif kwargs['method'] == "jelinek mercer":
            return get_prediction(kwargs['sentence'], 'jelinek mercer')
        elif kwargs['method'] == "witten bell":
            return get_prediction(kwargs['sentence'] ,'witten bell')
        elif kwargs['method'] == "absolute discounting":
            return get_prediction(kwargs['sentence'] ,'absolute discounting')
        else:
            return None


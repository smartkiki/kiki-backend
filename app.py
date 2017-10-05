import sys, json, requests
from flask import Flask, request
from nlp import response as nlp



app = Flask(__name__)



def message_handler():
		"""
		This method deals with handling understanding and responding to user's request.
		"""

		# get the user's input and store in user_input variable.
		user_input = "Hello"

		"""
		TEXT PROCESSING CODE
		Parses text and returns response string.
		"""
		nlp_handler = nlp.Response()
		responseText = nlp_handler.get_response(user_input)
		print(responseText)

		# responseText holds the output
		# responseText goes into text to speech API



message_handler()


@app.route('/')
def hello_world():
    return 'hello world'



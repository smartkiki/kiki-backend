import sys, json, requests
from flask import Flask, request
from nlp import response as nlp
from stt import speech_recognizer as stt
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask
from flask import jsonify
from detect_language import detect_lang

import argparse
import sys
import json

app = Flask(__name__)
 
@app.route('/')
def home():
	return '''Detect the language. Please provide a query in the link to detect the language. 
			  Write input query as "supported languages" to know the languages supported.'''

@app.route('/<user_input>')
def language_detector(user_input):
	if user_input == 'supported languages':
		return detect_lang.supported_languages(user_input)
	else:
		return detect_lang.detect_language(user_input)

	
		
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8082)

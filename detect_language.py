from __future__ import print_function
import argparse

import traceback
import logging

from langdetect import detect_langs
from langdetect import DetectorFactory 

from polyglot.detect import Detector
from polyglot.utils import pretty_list

#arguments needed
parser = argparse.ArgumentParser(description='Detect Language')
parser.add_argument('--str', type=str, required=True, help="Provide a string to detect language" )
parser.add_argument('--supported_language', '--sl', action='store_true', help='list of supported languages', default=False )

global input_text
input_text = parser.parse_args()
print("Input text: ", input_text.str)

def detect_language():

	#to make the results consistent
	DetectorFactory.seed = 0

	try:
		detected_language = str(detect_langs(input_text.str))
		detector = Detector(input_text.str, quiet=True)

		if detected_language[1:3]==detector.language.code :
			lang_detect = ("detcted language is: {}".format(detector.language.name))
		else:
			lang_detect = ("I think you speak {} but I am not sure. Please rewrite the sentence or write a longer sentence".format(detector.language.name))

	except Exception as e:
		#logging.error(traceback.format_exc())
		lang_detect = 'I am unsure of the languages. Please write a longer sentence.'
				
	return lang_detect

def supported_languages():
	if input_text.supported_language:
		print(pretty_list(Detector.supported_languages())) 


if __name__ == "__main__":
	lang_detect = detect_language()
	print (lang_detect)

	supported_languages()

	
	



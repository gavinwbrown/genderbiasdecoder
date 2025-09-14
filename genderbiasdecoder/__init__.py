"""
    This is the main entry point for the application
    Creates the flask application. No Database required.
    Imports routes module from the genderbiasdecoder package
"""

"""
    Gender bias decoder init
"""

import os
from flask import Flask
from assess import assess
from genderbiasdecoder.wordlists import feminine_coded_words
from genderbiasdecoder.wordlists import masculine_coded_words

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

from genderbiasdecoder import routes
"""
    This is the main entry point for the application
    Creates the flask application. No Database required.
    Imports routes module from the genderbiasdecoder package
"""

"""
    Gender bias decoder init
"""

from assess import assess
from genderbiasdecoder.wordlists import feminine_coded_words
from genderbiasdecoder.wordlists import masculine_coded_words
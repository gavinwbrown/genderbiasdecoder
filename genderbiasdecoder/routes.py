"""
    Will define route to page that loads at startup
"""

from flask import os
from flask import render_template, url_for
from genderbiasdecoder import app

@app.route("/")
# Initial page that loads at startup.
def home():
    return render_template("decoder.html")
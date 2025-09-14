# genderbiasdecoder

ALthough the gender bias decoder python package is free to use, this site's code is not to be used without the express written permission from myself.

## Overview

Gender Bias Decoder is a single page web app that scans inputted text for any unconscious bias. Any problems are highlighted in pink for female bias and blue for male bias. Text free from bias is better for emails, job adverts etc, ensuring that people are not put off by any bias. Running Python in Flask with HTML and Bootstrap 5.3.8 for styling the front-end.

## Technologies

[Flask](https://flask.palletsprojects.com/en/stable/) - a lightweight WSGI web application framework.

[Bootstrap](https://getbootstrap.com) - powerful, extensible, and feature-packed frontend toolkit.

[Doteveryone](https://github.com/Doteveryone) - Python package gender bias decoder. MIT licence.

## Build Process

<shift><command>p then select Python:Create Environment and select venv
'source /Users/gavb/VSCode/genderbiasdecoder/.venv/bin/activate' activate virtual environment (should see (.venv) at start of terminal command prompt)
python3
pip install --upgrade pip
pip install flask
pip install python.env

create .env and env.py and add environment variables to them.

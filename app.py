# name the .py file app.py or wsgi.py and execute 'flask run' command, browse to localhost:5000/
from flask import Flask
from markupsafe import escape  # use {escape(VAR)} function to protect against injection attacks

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Home Page</h1>"

@app.route('/hello')
def hello_world(): # browse to localhost:5000/hello
    return "<p>Hello, World!</p>"

@app.route('/hello/') # this is a different URL -
def hello_world_final_slash():
    return "<p>Hello, World!///</p>"
#  adding final slash makes it canonical - same URL resolves to same page with or without final slash but will duplicate pages from search engine point of view
#  what is best practice?

# add vars to urls with <vartype:varname> converter i.e. localhost:5000//myurl/<int:intvarname>
'''
converter types:
string
int
float
path
uuid
''
'

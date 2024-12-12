import re
from datetime import datetime


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")


def home():
    return "Hello , Flask!"

@app.route("/hello/")
@app.route("/hello/Ali")

def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X") # 'Wednesday, 31 October, 2018 at 18:13:39'
    '''
    Different date formats
    
        now.strftime("%a, %d %B, %Y at %X")
        'Wed, 31 October, 2018 at 18:13:39'
        now.strftime("%a, %d %b, %Y at %X")
        'Wed, 31 Oct, 2018 at 18:13:39'
        now.strftime("%a, %d %b, %y at %X")
        'Wed, 31 Oct, 18 at 18:13:39'

    '''
    match_object = re.match("[a-zA-Z]+", name)
    
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
        
    content = "Hello There , " +clean_name + "! It is  "+ formatted_now
    return content

@app.route("/hello_template/?names=John")
def hello_template(names=None):
    return render_template("hello_there.html", name = names, date = datetime.now())
import re
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Validate the name parameter
    if name:
        match_object = re.match("[a-zA-Z]+", name)
        clean_name = match_object.group(0) if match_object else "Friend"
    else:
        clean_name = "Friend"

    content = f"Hello There, {clean_name}! It is {formatted_now}."
    return content

@app.route("/hello_template/")
def hello_template():
    # Retrieve the 'name' parameter from the query string
    names = request.args.get("names", "Friend")
    return render_template("hello_there.html", name=names, date=datetime.now())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    

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
    """
    Different date formats
       now.strftime("%a, %d %B, %Y at %X")
        'Wed, 31 October, 2018 at 18:13:39'
        now.strftime("%a, %d %b, %Y at %X")
        'Wed, 31 Oct, 2018 at 18:13:39'
        now.strftime("%a, %d %b, %y at %X")
        'Wed, 31 Oct, 18 at 18:13:39'
    """

    # Validate the name parameter
    if name:
        match_object = re.match(
            "[a-zA-Z]+$", name
        )  # # Ensure only alphabets are allowed
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
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host="127.0.0.1", port=5000, debug=True)
    app.run(debug=True)

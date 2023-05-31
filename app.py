#!python3

from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)


@app.route('/')
def rootpage():
    return render_template("index.html")

# Arrays of quotes (add more)
quotes = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
    {"quote": "Life is 10% what happens to us and 90% how we react to it.", "author": "Charles R. Swindoll"}
    # Add more quotes here
]

# Route to generate a random quote
@app.route("/random-quote", methods=['GET', 'POST'])
def random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

@app.route('/login')
def login():
    return('Username details required')

@app.route('/method', methods=['GET', 'POST'])
def method ():
    if request.method == 'POST':
        return 'Innovation distinguishes between a leader and a follower., "author": Steve Jobs'
    else:
        return 'Do you need some random quotes'

app.run()

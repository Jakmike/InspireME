from flask import Flask, jsonify
import random

app = Flask(__name__)

# Arrays of quotes (add more)
quotes = [
    {"quote": "the only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
    {"quote": "Life is 10% what happens to us and 90% how we react to it.", "author": "Charles R. Swindoll"}
    # Add more quotes here
]

# Route to generate a random quote
@app.route("/random-quote")
def random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == "__main__":
    app.run()
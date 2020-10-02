import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route('/buzz')
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

@app.route('/')
def home():
    return '<html><body><h1>Hi there! Welcome to this test demo!</h1></body></html>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

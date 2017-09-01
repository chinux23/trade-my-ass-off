import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    '''
    index page
    '''
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

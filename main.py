import os
from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    '''
    index page
    '''
    return render_template('list.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

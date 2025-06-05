from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

#list the urls of your app
@app.route('/')
@app.route('/index')

#define the contents of the index page
def index():
    #use index html template
    return render_template('index.html')

if __name__ == "__main__":
    #use waitress to serve our local app
    serve(app, host="0.0.0.0", port=8000)
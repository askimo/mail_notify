from flask import Flask
from flask import request
from flask import url_for
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Test In Python"
@app.route('/hello')
def show_hello():
    return "<h1>Just is a Test Webpage."
@app.route('/var/<var>')
def show_var(var):
    return "<h1>Test var In Flask:var = %s"%var

@app.route('/url/<url>')
def show_url(url):
    return "<h1>URL For %s is %s"%(url,url_for(url))


if __name__ == "__main__":
    app.run()

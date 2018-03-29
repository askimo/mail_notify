from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
import json
import mail
app = Flask(__name__)


@app.route('/hello')
def show_hello():
    return "<h1>Just is a Test Webpage."
@app.route('/var/<var>')
def show_var(var):
    return "<h1>Test var In Flask:var = %s"%var
@app.route('/url/<url>')
def show_url(url):
    return "<h1>URL For %s is %s"%(url,url_for(url))


@app.route('/')
def index():
    return render_template("index.html")
#post setting to /notify
@app.route('/setting',methods=['POST','GET'])
def setting():
    if request.method == 'GET':
        return render_template("setting.html")
    print(dict(request.form))
    with open('config.json','w') as f:
        f.write(json.dumps(request.form))
    return "<h1>setting finished."


#get title and content to /notify
@app.route('/notify')
def notify():
    title=request.args["title"]
    content=request.args["content"]
    print("title:%s/n/rcontent:%s"%(title,content))
    try:
        mail.sendmail(title,content)
    except Exception as e:
        return "<h1>Exception accured while sending mail:<br><h2><font color='red'>%s</font>"%e
    return "<h1><font  color='green'>Success sending mail notify</font>."

if __name__ == "__main__":
    app.run()

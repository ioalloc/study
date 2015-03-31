from flask import Flask
from flask import request
from gi.repository import Notify

app = Flask(__name__)
Notify.init('hello world')

@app.route('/')
def hello():
	return 'hello'

@app.route('/tasker')
def taskerhander():
	title = request.form.get('t','')
	Hello=Notify.Notification.new (title,"This is an example notification.","dialog-information")
	Hello.show ()
	return 'tasker'

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
from flask import Flask
from flask import request
from gi.repository import Notify
import pprint

app = Flask(__name__)
Notify.init('hello world')

@app.route('/')
def hello():
	return 'hello'

@app.route('/tasker')
def taskerhander():
	#pprint.pprint(request.args.get('t'))
	title = request.args.get('t','')
	Hello=Notify.Notification.new(title,"","information")
	Hello.show()
	#dump(request)
	return 'title'

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
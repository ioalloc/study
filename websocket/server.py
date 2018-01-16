#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

__author__ = 'xiwei'

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def get_index_page():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print message
    emit('message', 'test')

def send():
    while 1:
        socketio.emit('message', time.time())
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=send).start()
    socketio.run(app, debug=True)

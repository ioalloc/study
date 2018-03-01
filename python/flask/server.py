#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import time
import os


from multiprocess import Manager, Process
from multiprocess.queues import Queue, Full, Empty
from multiprocess.synchronize import Event
from coloredlogs import install


from flask import Flask, request


MAX_QUEUE_SIZE = 100


install()
app = Flask(__name__)
logger = logging.getLogger('Task')

manager = Manager()

queue = manager.Queue(MAX_QUEUE_SIZE)  # type: Queue

process_map = {}


class Message(dict):
    """
    message
    """

    def __init__(self, mtype, data, error_event, **kwargs):
        """

        :param mtype:
        :param data:
        :param error_event:
        :type error_event: Event
        :param kwargs:
        """
        super(Message, self).__init__(**kwargs)
        self.data = data
        self.error = error_event


def consume():
    """
    :return
    """
    while True:
        try:
            message = queue.get(timeout=1)   # type: Message
            logger.info("Consume message: {}, qsize: {}".format(message.data, queue.qsize()))
            message.error.set()
        except Empty:
            logger.warning("Queue was empty")


def product():
    """

    :return:
    """
    error = manager.Event()  # type: Event
    i = 0
    while True:
        time.sleep(1)
        try:
            queue.put(Message(1, "%s - %s" % (os.getpid(), i), error_event=error))
            i += 1
        except Full:
            pass
        if error.is_set():
            break


@app.route('/')
def index():
    """
    :return:
    """
    return "qsize: {}, process: {}".format(queue.qsize(), process_map)


@app.route('/<process>/<int:pid>', methods=['GET', 'DELETE'])
@app.route('/<process>', methods=['POST'])
def v_consume(process=None, pid=None):
    """
    :return:
    """
    if request.method == 'GET':
        if pid in process_map:
            return str(process_map[pid])
        return "consume not found", 404
    elif request.method == 'DELETE':
        p = process_map.get(pid)  # type: Process
        if p:

            p.terminate()
            del process_map[pid]
            return "ok"
        else:
            return "consume not found", 404
    else:
        if process is 'product':
            p = Process(target=product, name='product')
        else:
            p = Process(target=consume, name='consume')
        p.start()
        process_map[p.pid] = p
        return str(p.pid)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

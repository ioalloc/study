#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

import time
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

tornado.options.parse_command_line()


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Hello, world")
        self.finish()


class NoBlockingHnadler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(10)
        self.write('Blocking Request')


class BlockingHnadler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(10)
        self.write('Blocking Request')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/block", BlockingHnadler),
        (r"/noblock", NoBlockingHnadler),
    ], autoreload=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

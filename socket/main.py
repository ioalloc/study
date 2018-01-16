#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from socket import socket
from select import select
import colorama
colorama.init(autoreset=True)


def server():
    sock = socket()
    sock.bind(('127.0.0.1', 4000))
    sock.listen(5)

    sockets = {sock: ('127.0.0.1', 4000)}
    while True:
        readable, writable, exception = select(sockets.keys(), [], [])
        for s in readable:  # type: socket
            if s is sock:
                connection, address = s.accept()
                print colorama.Fore.GREEN + 'connect: ', address
                sockets[connection] = address
            else:
                data = s.recv(1024)
                if not data:
                    print colorama.Fore.RED + 'disconnect: ', sockets[s]
                    sockets.pop(s, None)
                    s.close()
                print colorama.Fore.GREEN + "receive " + str(sockets[s]) + ': ', data.replace('\r\n', '')


def client():
    pass


if __name__ == '__main__':
    import sys
    if sys.argv[-1] == 'server':
        server()
    else:
        print 'client'

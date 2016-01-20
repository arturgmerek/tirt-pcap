#!/usr/bin/env python
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
TCP_TUPLE = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 4096


def get_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def get_and_bind_socket(port=0):
    s = get_socket()
    if port is 0:
        s.bind(TCP_TUPLE)
    else:
        s.bind((TCP_IP, port))
    return s

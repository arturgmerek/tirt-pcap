#!/usr/bin/env python
import dpkt
import socket_manager as sm
import pygal_charts as pc


def filter_eth_type():
    s_in = sm.get_and_bind_socket(5008)
    s_in.listen(1)
    conn, address = s_in.accept()
    while 1:
        data = conn.recv(sm.BUFFER_SIZE)
        if not data:
            pc.chart_eth_type()
            conn.close()
            break
        eth = dpkt.ethernet.Ethernet(data)
        pc.data_eth_type(str(eth.type))


if __name__ == '__main__':
    filter_eth_type()

#!/usr/bin/env python
import dpkt
import print_packets
import socket_manager as sm
import pygal_charts as pc


def filter_eth():
    s_in = sm.get_and_bind_socket()
    s_in.listen(1)
    conn, address = s_in.accept()

    s_out = sm.get_socket()
    s_out.connect((sm.TCP_IP, 5006))

    while 1:

        pkt = conn.recv(sm.BUFFER_SIZE)
        if not pkt:
            pc.chart_eth_route()
            pc.chart_eth_type()
            conn.close()
            s_out.close()
            break
        eth = dpkt.ethernet.Ethernet(pkt)
        pc.data_eth_route(print_packets.mac_addr(eth.src), print_packets.mac_addr(eth.dst))
        pc.data_eth_type(str(eth.type))
        s_out.send(pkt)


if __name__ == '__main__':
    filter_eth()

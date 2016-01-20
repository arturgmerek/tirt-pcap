#!/usr/bin/env python
import dpkt
import print_packets
import socket_manager as sm
import pygal_charts as pc


def filter_ip_route():
    s_in = sm.get_and_bind_socket()
    s_in.listen(1)
    conn, address = s_in.accept()

    s_out = sm.get_socket()
    s_out.connect((sm.TCP_IP, 5006))

    while 1:
        pkt = conn.recv(sm.BUFFER_SIZE)
        if not pkt:
            pc.chart_ip_route()
            conn.close()
            s_out.close()
            break
        ip_route(pkt)
        s_out.send(pkt)


def ip_route(data):
    eth = dpkt.ethernet.Ethernet(data)
    ip = eth.data
    pc.data_ip_route(print_packets.ip_to_str(ip.src), print_packets.ip_to_str(ip.dst))


if __name__ == '__main__':
    filter_ip_route()

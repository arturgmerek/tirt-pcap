#!/usr/bin/env python
import dpkt
import socket_manager as sm
import pygal_charts as pc


def filter_ip_aux():
    s_in = sm.get_and_bind_socket(5006)
    s_in.listen(1)
    conn, address = s_in.accept()

    s_out = sm.get_socket()
    s_out.connect((sm.TCP_IP, 5007))

    while 1:
        pkt = conn.recv(sm.BUFFER_SIZE)
        if not pkt:
            pc.chart_ip_aux()
            conn.close()
            s_out.close()
            break
        ip_aux(pkt)
        s_out.send(pkt)


def ip_aux(data):
    eth = dpkt.ethernet.Ethernet(data)
    ip = eth.data
    pc.data_ip_aux(str(ip.len), str(ip.ttl))


if __name__ == '__main__':
    filter_ip_aux()

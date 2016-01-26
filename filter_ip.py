#!/usr/bin/env python
import dpkt
import print_packets
import socket_manager as sm
import pygal_charts as pc


def filter_ip():
    packets = 0
    s_in = sm.get_and_bind_socket(5006)
    s_in.listen(1)
    conn, address = s_in.accept()

    s_out = sm.get_socket()
    s_out.connect((sm.TCP_IP, 5007))

    while 1:
        try:
            pkt = conn.recv(sm.BUFFER_SIZE)

            if not pkt:
                pc.chart_ip_route()
                pc.chart_ip_aux()
                conn.close()
                s_out.close()
                break
            packets += 1
            eth = dpkt.ethernet.Ethernet(pkt)
            ip = eth.data
            pc.data_ip_route(print_packets.ip_to_str(ip.src), print_packets.ip_to_str(ip.dst))
            pc.data_ip_aux(str(ip.len), str(ip.ttl))
            s_out.send(pkt)
        except AttributeError:
            pass
    print(packets)


if __name__ == '__main__':
    filter_ip()

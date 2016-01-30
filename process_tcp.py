#!/usr/bin/env python
import dpkt
import socket_manager as sm


def process_tcp():
    packets = 0
    s_in = sm.get_and_bind_socket(5007)
    s_in.listen(1)
    conn, address = s_in.accept()

    # s_out = sm.get_socket()
    # s_out.connect((sm.TCP_IP, 5007))

    while 1:
        try:
            pkt = conn.recv(sm.BUFFER_SIZE)
            if not pkt:
                conn.close()
                break
            eth = dpkt.ethernet.Ethernet(pkt)
            ip = eth.data
            tcp = ip.data
            # http = dpkt.http.Response(tcp.data)
            print(tcp)

        except AttributeError:
            pass
    print(packets)


if __name__ == '__main__':
    process_tcp()

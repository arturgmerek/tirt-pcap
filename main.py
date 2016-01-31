#!/usr/bin/env python
import subprocess


if __name__ == '__main__':
    subprocess.Popen(['python', 'process_tcp.py'])  # port_in: 5007
    subprocess.Popen(['python', 'filter_ip.py'])  # port_in: 5006 port_out: 5007
    subprocess.Popen(['python', 'filter_eth.py'])  # port_in: 5005 port_out: 5006
    s = subprocess.Popen(['python', 'pcap_loader.py'], stdout=subprocess.PIPE)  # port_out: 5005
    out, err = s.communicate()
    print(out)


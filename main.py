#!/usr/bin/env python
import subprocess


if __name__ == '__main__':
    s = subprocess.Popen(['python', 'process_tcp.py'], stdout=subprocess.PIPE)  # port_in: 5007
    subprocess.Popen(['python', 'filter_ip.py'])  # port_in: 5006 port_out: 5007
    subprocess.Popen(['python', 'filter_eth.py'])  # port_in: 5005 port_out: 5006
    subprocess.Popen(['python', 'pcap_loader.py'])  # port_out: 5005
    out, err = s.communicate()
    print(out)


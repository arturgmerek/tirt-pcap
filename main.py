#!/usr/bin/env python
import subprocess


if __name__ == '__main__':
    try:
        s = subprocess.Popen(['python', 'eth_type.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # port_in: 5008
        subprocess.Popen(['python', 'eth_route.py'])  # port_in: 5007 port_out: 5008
        subprocess.Popen(['python', 'ip_aux.py'])  # port_in: 5006 port_out: 5007
        subprocess.Popen(['python', 'ip_route.py'])  # port_in: 5005 port_out: 5006
        subprocess.Popen(['python', 'pcap_loader.py'])  # port_out: 5005
    except OSError as e:
        print("OSError: ", e.message)
    except ValueError as e:
        print("ValueError: ", e.message)

    out, err = s.communicate()
    print(out)
    print(err)

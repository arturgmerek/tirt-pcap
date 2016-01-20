#!/usr/bin/env python
import pygal
from collections import Counter

IP_SRC = []
IP_DST = []
IP_LEN = []
IP_TTL = []

ETH_SRC = []
ETH_DST = []
ETH_TYPE = []


def data_ip_route(ip_src, ip_dst):
    global IP_SRC
    global IP_DST

    IP_SRC.append(ip_src)
    IP_DST.append(ip_dst)


def chart_ip_route():
    global IP_SRC
    global IP_DST

    chart = pygal.Bar()

    for ip_src in Counter(IP_SRC).keys():
        chart.add("Src:" + ip_src, Counter(IP_SRC)[ip_src])

    for ip_dst in Counter(IP_DST).keys():
        chart.add("Dst:" + ip_dst, Counter(IP_DST)[ip_dst])

    chart.render_to_file('ip_route.svg')


def data_eth_route(eth_src, eth_dst):
    global ETH_SRC
    global ETH_DST

    ETH_SRC.append(eth_src)
    ETH_DST.append(eth_dst)


def chart_eth_route():
    global ETH_SRC
    global ETH_DST

    chart = pygal.Bar()

    for src in Counter(ETH_SRC).keys():
        chart.add("Src:" + src, Counter(ETH_SRC)[src])

    for dst in Counter(ETH_DST).keys():
        chart.add("Dst:" + dst, Counter(ETH_DST)[dst])

    chart.render_to_file('eth_route.svg')


def data_ip_aux(ip_len, ip_ttl):
    global IP_LEN
    global IP_TTL

    IP_LEN.append(ip_len)
    IP_TTL.append(ip_ttl)


def chart_ip_aux():
    global IP_LEN
    global IP_TTL

    chart = pygal.Bar()

    for ip_len in Counter(IP_LEN).keys():
        chart.add("Len:" + ip_len, Counter(IP_LEN)[ip_len])

    for ip_ttl in Counter(IP_TTL).keys():
        chart.add("TTL:" + ip_ttl, Counter(IP_TTL)[ip_ttl])

    chart.render_to_file('ip_aux.svg')


def data_eth_type(eth_type):
    global ETH_TYPE

    ETH_TYPE.append(eth_type)
    print (eth_type)


def chart_eth_type():
    global ETH_TYPE

    chart = pygal.Bar()

    for eth_type in Counter(ETH_TYPE).keys():
        chart.add("Type:" + eth_type, Counter(ETH_TYPE)[eth_type])

    chart.render_to_file('eth_type.svg')

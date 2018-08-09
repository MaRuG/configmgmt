#! /usr/bin/env python
# -*- coding: utf-8 -*-
import napalm
import pprint
import sys
import datetime
import re

def now_time():
    ####################
    # get now
    ####################
    datetime.datetime.today()#時間まで
    datetime.date.today().isoformat()#フォーマットの指定
    now = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")#フォーマットの指定
    return now

def get_config(os, addr, name, password, port):
####################
# get driver
####################
    if port != None:
        driver = napalm.get_network_driver(os)
        optional_args = {'port': port}
        device = driver(
            hostname=addr,
            username=name,
            password=password,
            optional_args=optional_args)
    elif port == None:
        driver = napalm.get_network_driver(os)
        device = driver(
            hostname=addr,
            username=name,
            password=password)

    device.open()

    config = device.get_config()
    config = pprint.pformat(config, indent=4)

    print('Close session: ',)
    device.close()
    return config

def write_config(configs):
    now = now_time()
    ####################
    # write config
   ####################
    matchtext = re.findall(r"host-name\s[a-zA-Z0-9]*", configs) 
    hostname = str(set(matchtext)).replace("host-name ", "")
    hostname =  re.sub(r"[\{\}\']", "", hostname)

    with open('configs/%s_%s.config' % (hostname, now), "w") as f:
        f.write(configs)
# args = sys.argv
# print(args)
# os = args[1]
# addr = args[2]
# name = args[3]
# password = args[4]
# port = args[5]
# config = get_config(os, addr, name, password, port)
# print(config)

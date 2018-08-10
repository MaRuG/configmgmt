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

def device_load(os, addr, name, password, port):
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
        
    return device

def get_config(device):
    device.open()

    config = device.get_config()
    config = config["running"]

    print('Close session: ',)
    device.close()
    return config

def add_config(device, conf):
    device.open()
    try:
        device.load_merge_candidate(config=conf)
    except:
        device.load_merge_candidate(filename=conf)
        
    compare = device.compare_config()
    device.close()

    return compare

def commit(device, choice):
    device.open()
    if choice == 'commit_ok':
        device.commit_config()
    elif choice == 'commit_no':
        device.discard_config()

    # config = get_config()
    device.close()
    # return config


def write_config(configs, filename):
    with open('configs/%s.config' % (filename), "w") as f:
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

# -*- coding: utf-8 -*-

# 2019/1/16 0016 下午 1:41     

__author__ = 'RollingBear'

import threading
import time
import random


def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print('\033[32;1m---green light on---\033[0m')
        elif count < 13:
            print('\033[33;1m---yellow light on---\033[0m')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('\033[31;1m---red light on---\033[0m')
        else:
            count = 0
            event.set()
        time.sleep(1)
        count += 1


def car(n):
    while True:
        time.sleep(random.randrange(3, 10))
        if event.isSet():
            print("car [%s] is running..." % n)
        else:
            print('car [%s] is waiting for the red light...' % n)
            event.wait()


if __name__ == '__main__':
    car_list = ['car_1', 'car_2', 'car_3', 'car_4']
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in car_list:
        t = threading.Thread(target=car, args=(i,))
        t.start()

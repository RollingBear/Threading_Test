# -*- coding: utf-8 -*-

# 2019/1/16 0016 上午 11:11     

__author__ = 'RollingBear'

import threading
import time


def Seeker(cond, name):
    time.sleep(2)
    cond.acquire()
    print('%s close eyes' % name)
    # 1
    cond.notify()
    # 2
    cond.wait()
    for i in range(3):
        print('%s is finding' % name)
        time.sleep(2)
    # 3
    cond.notify()
    cond.release()
    print('%s win' % name)


def Hider(cond, name):
    cond.acquire()
    # 1
    cond.wait()
    for i in range(2):
        print('%s is hiding' % name)
        time.sleep(3)
    print('%s is already hided' % name)
    # 2
    cond.notify()
    # 3
    cond.wait()
    cond.release()
    print('%s has been findes' % name)


if __name__ == '__main__':
    cond = threading.Condition()
    seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
    hider = threading.Thread(target=Hider, args=(cond, 'hider'))
    seeker.start()
    hider.start()

# -*- coding: utf-8 -*-

# 2019/1/16 0016 下午 2:48     

__author__ = 'RollingBear'

import threading
import time


def run(n):
    print('-' * 30)
    print('Now Pid is %s' % threading.current_thread().ident)
    print('Main Pid is %s' % threading.main_thread().ident)
    print('Now thread is %s' % threading.current_thread().getName())
    print('Main thread is %s' % threading.main_thread().getName())


if __name__ == '__main__':
    threading.main_thread().setName('---MainThread---')
    for i in range(3):
        thread_alive = threading.Thread(target=run, args=(i,))
        thread_alive.start()
        time.sleep(2)
    thread_alive.join()

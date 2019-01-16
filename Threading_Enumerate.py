# -*- coding: utf-8 -*-

# 2019/1/16 0016 下午 2:34     

__author__ = 'RollingBear'

import threading
import time


def run(n):
    thread = threading.current_thread()
    thread.setName('Thread-***%s***' % n)
    print('-' * 30)
    print('Pid is: %s' % thread.ident)
    print('ThreadName is: %s' % threading.enumerate())
    time.sleep(2)


if __name__ == '__main__':
    threading.main_thread().setName('---MainThread---')
    for i in range(3):
        thread_alive = threading.Thread(target=run, args=(i,))
        thread_alive.start()
    thread_alive.join()
    print('\n%s thread is done' % threading.current_thread().getName())

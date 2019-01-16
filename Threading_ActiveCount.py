# -*- coding: utf-8 -*-

# 2019/1/16 0016 下午 2:09     

__author__ = 'RollingBear'

import threading
import time


def run():
    thread = threading.current_thread()
    print('%s is running...' % thread.getName())
    time.sleep(10)


if __name__ == '__main__':
    # print('The current number of threads is: %s' % threading.active_count())
    for i in range(10):
        print('The current number of threads is: %s' % threading.activeCount())
        thread_alive = threading.Thread(target=run, name='Thread-***%s***' % i)
        thread_alive.start()
    thread_alive.join()
    print('\n%s thread is done...' % threading.current_thread().getName())

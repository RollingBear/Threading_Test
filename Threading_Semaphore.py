# -*- coding: utf-8 -*-

# 2019/1/16 0016 上午 11:52     

__author__ = 'RollingBear'

import threading
import time


def run(n):
    # 获得信号量，信号量-1
    semaphore.acquire()
    time.sleep(1)
    print('run the thread: %s' % n)

    semaphore.release()
    # 多次释放信号量时每次释放信号量+1
    # semaphore.release()


if __name__ == '__main__':
    num = 0
    # 最多允许2个线程同时运行(即计数器值)；在多次释放信号量后，计数器值增加后每次可以运行的线程数也会增加
    semaphore = threading.Semaphore(2)
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

    while threading.active_count() != 1:
        pass
        # print(threading.active_count())
    else:
        print('all thread done')
        print(num)

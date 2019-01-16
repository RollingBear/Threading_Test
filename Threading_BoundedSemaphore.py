# -*- coding: utf-8 -*-

# 2019/1/16 0016 下午 1:24     

__author__ = 'RollingBear'

import threading
import time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread %s' % n)
    semaphore.release()
    # semaphore.release()
    # 如果再次释放信号量，信号量加一，这是超过限定的信号量数目，这时会报错ValueError: Semaphore released too many times


if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(2)

    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print('all thread done')
    print(num)

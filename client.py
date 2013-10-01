#!/usr/bin/env python
import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2

def fetch(num):
    response = urllib2.urlopen('http://127.0.0.1/' + str(num))

def asynchronous():
    threads = []
    for i in range(1,10):
        print "Spawning " + str(i)
        threads.append(gevent.spawn(fetch, i))
        gevent.sleep(0.1)
    gevent.joinall(threads)

if __name__ == '__main__':
    print('Asynchronous:')
    asynchronous()

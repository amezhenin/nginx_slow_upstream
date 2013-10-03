#!/usr/bin/env python
from flask import Flask
import time

app = Flask(__name__)
prev_num = 0

# setup logging
import logging
logger = logging.getLogger('server')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')

file_hdlr = logging.FileHandler('server.log')
console = logging.StreamHandler()

file_hdlr.setFormatter(formatter)
console.setFormatter(formatter)

logger.addHandler(file_hdlr) 
logger.addHandler(console)

logger.setLevel(logging.DEBUG)

@app.route('/<int:num>')
def hello_world(num):
    global prev_num
    time.sleep(1)
    logger.debug('num-prev_num, num: %d - %d', num - prev_num, num)  
    prev_num = num
    return 'Hello %s' % num

if __name__ == '__main__':
    #app.debug = True
    app.run('127.0.0.1', 8000)

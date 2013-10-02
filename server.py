#!/usr/bin/env python
from flask import Flask
import time
app = Flask(__name__)

prev_num = 0

@app.route('/<int:num>')
def hello_world(num):
    global prev_num
    time.sleep(1)
    # log request param  
    with open('log', 'a') as fd:
        fd.write('%d - %d \n'%(num - prev_num ,num))
    prev_num = num
    return 'Hello %s' % num

if __name__ == '__main__':
    #app.debug = True
    app.run('127.0.0.1', 8000)

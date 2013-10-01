from flask import Flask
import time
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    time.sleep(1)
    with open('log', 'a') as fd:
        fd.write(name + '\n')
    return 'Hello %s' % name

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 8000)

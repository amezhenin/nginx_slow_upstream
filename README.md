nginx_slow_upstream
===================
This is small test for Nginx upstream mechanism. For this reason I wrote 
**server.py** and **client.py** scripts. 

## server.py
Python script, that use Flask to server requests. Server server will sleep for
1 second, before returning response.

## client.py
Python script, that use Gevent to spawn a asyncronous requests to server. Client
will sleep for 0.1 second, before spawning next request. 

## nginx.conf
Copy **nginx.conf** to sites-enabled folder

## requirements.txt
This is requirements for **server.py** and **client.py**. You can install them 
with:

    pip install -r requirements.txt
    
## server.log
**server.log** file is created by **server.py** to log request params in order they 
were passed from Nginx to **server.py**.

# Results
TBD

import random
import time
from flask import Flask
from prometheus_client import start_http_server, generate_latest, Gauge, Summary, Counter, Histogram

app = Flask(__name__)

HTTP_REQUESTS =  Counter('HTTP_REQUESTS', 'Counter to show the total HTTP request amount')
AUTHENTICATED_USERS =  Counter('AUTHENTICATED_USERS', 'Number of authenticated users')
HTTP_REQUESTS_LATENCY = Histogram('HTTP_LATENCY', 'Histogram to show request latency')

@app.before_request
def before_request():
    HTTP_REQUESTS.inc(1)
    # HTTP_REQUESTS_LATENCY.observe(5.4[])  

@app.after_request
def after_request(response):
    return response

@app.get('/metrics') # The default Prometheus HTTP path to pull data from
def metrics():
    return generate_latest(), 200

@app.post('/hello')
def get_hello():
    return 'hello world!'

@app.get('/math')
def get_math():
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    return f'{x} + {y} = ?'

app.run(port=8881)

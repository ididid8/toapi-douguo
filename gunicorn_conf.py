import os
import multiprocessing

LOG_PATH = os.path.join(os.getcwd(), 'log/')

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

bind = '0.0.0.0:5000'
graceful_timeout = 30
preload_app = True
max_requests = 1000
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2

loglevel = 'info'
accesslog = os.path.join(LOG_PATH, 'access.log')
errorlog = os.path.join(LOG_PATH, 'error.log')

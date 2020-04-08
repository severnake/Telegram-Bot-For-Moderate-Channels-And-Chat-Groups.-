import redis  

"""REDIS DATABASE UTILITY"""

try:
    rdb = redis.Redis(host='localhost', port=6379, decode_responses=True, socket_connect_timeout=1)
    rdb.ping()
except Exception as e:
    print(e, '\nPlease make sure redis-server is installed and up running')
    exit()
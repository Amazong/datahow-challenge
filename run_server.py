from gevent.pywsgi import WSGIServer
from app.count_unique_ips import app

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
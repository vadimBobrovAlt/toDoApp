import json
from urllib import request


class apiClass():

    def __init__(self):
        self.url = 'http://127.0.0.1:5000/api/v1/'

    def post(self, url, body, token=None):
        req = request.Request(self.url + url, data=json.dumps(body).encode())
        req.add_header('Content-Type', 'application/json')
        if token is not None:
            req.add_header('Authorization', 'JWT ' + token)
        res = request.urlopen(req)
        res = res.read()
        res = json.loads(res.decode('utf-8'))
        return res

    def get(self, url, token=None):
        req = request.Request(self.url + url)
        req.add_header('Content-Type', 'application/json')
        if token is not None:
            req.add_header('Authorization', 'JWT ' + token)
        res = request.urlopen(req)
        res = res.read()
        res = json.loads(res.decode('utf-8'))
        return res
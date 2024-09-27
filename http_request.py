from http.client import  HTTPSConnection
from json import loads


def get(uri, path, headers={}):
    conn = HTTPSConnection(uri)
    conn.request("GET", path, headers=headers)
    return conn.getresponse().read()

def getJSON(uri, path, headers={}):
    conn = HTTPSConnection(uri)
    conn.request("GET", path, headers=headers)
    return json.loads(conn.getresponse().read())

import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds051990.mlab.com:51990/api
host = "ds051990.mlab.com"
port = 51990
db_name = "api"
username = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())

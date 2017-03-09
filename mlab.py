import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds123400.mlab.com:23400/testapi
host = "ds123400.mlab.com"
port = 23400
db_name = "testapi"
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

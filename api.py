import json
from fakeDatabase import FakeDB

def v1_perform(action,build_type,item):
    ret = ''
    if action == 'list':
        if build_type == 'r':
            ret = json.dumps(FakeDB('static/r').by_device(item))
        elif build_type == 'n':
            ret = json.dumps(FakeDB('static/n').by_device(item))
    return ret

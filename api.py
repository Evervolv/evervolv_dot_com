import json
from fakeDatabase import FakeDB

def v1_perform(action,build_type,item):
    ret = ''
    if action == 'list':
        if build_type == 'release':
            ret = json.dumps(FakeDB('static/r').by_device(item))
        elif build_type == 'nightly':
            ret = json.dumps(FakeDB('static/n').by_device(item))
    return ret

def v1_get(build_type,item):
    ret = None
    if item.endswith('.zip'):
      if build_type == 'release':
          ret = FakeDB('static/r').by_name(item)
      elif build_type == 'nightly':
          ret = FakeDB('static/r').by_name(item)
    else:
        pass
    return ret

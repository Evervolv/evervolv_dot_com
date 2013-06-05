import json
import fakeDatabase

def v1_perform(action,build_type,item):
    ret = ''
    if action == 'list':
        builds = fakeDatabase.by_device(item)
        if build_type == 'r':
            ret = json.dumps(builds[1])
        elif build_type == 'n':
            ret = json.dumps(builds[0])
    return ret

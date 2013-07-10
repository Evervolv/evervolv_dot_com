import json
import fakeDatabase
import devices

def v1_perform(action,build_type,device):
    ret = None
    if action == 'list':
        if device in devices.devices():
            builds = fakeDatabase.by_device(device)
            if build_type.lower() == 'n':
                ret = json.dumps(builds[0])
            elif build_type.lower() == 'r':
                ret = json.dumps(builds[1])
            elif build_type.lower() == 't':
                ret = json.dumps(builds[2])
            elif build_type.lower() == 'g':
                ret = json.dumps(builds[3])
    return ret

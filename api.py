import json
import fakeDatabase
import devices

def v1_perform(action,build_type,device):
    ret = None
    if action == 'list':
        if device in devices.devices():
            builds = fakeDatabase.by_device(device)
            if build_type.lower() == 'n':
                if builds[0]:
                    ret = json.dumps(builds[0])
            elif build_type.lower() == 'r':
                if builds[1]:
                    ret = json.dumps(builds[1])
    return ret

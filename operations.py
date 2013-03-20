# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import os
from devices import device_codename
from fakeDatabase import FakeDB

def locate_by_device(device=None,location='static/r'):
    ret = []
    if device and os.path.exists(location):
        device_dir = device_codename(device)
        for (path,dirs,files) in os.walk(os.path.join(location, device_dir)):
            for f in sorted(files, reverse=True):
                if f.endswith('.zip'):
                    ret.append({'device':device, 'name': f,
                        'location':os.path.join(path,f)})
    return ret

def find_builds(device=None):
    if device:
        nightly = FakeDB().get_device(device=device)
        release = locate_by_device(device=device)
        builds = { 'release': release, 'nightly': nightly }
    else:
        builds = { 'release':[],'nightly':[] }
    return builds

def get_screenshots(location='static/img/screenshots'):
    screens = []
    try:
        screens = os.listdir(location)
    except OSError as e:
        pass
    return screens

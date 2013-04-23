# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import os
from fakeDatabase import FakeDB

# Used by Devices
def find_builds(device=None):
    if device:
        nightly = FakeDB('static/n').by_device(device=device)
        release = FakeDB('static/r').by_device(device=device)
        builds = { 'release': release, 'nightly': nightly }
    else:
        builds = { 'release':[],'nightly':[] }
    return builds

# Used by Features
def get_screenshots(location='static/img/screenshots'):
    screens = []
    try:
        screens = os.listdir(location)
    except OSError as e:
        pass
    return screens

# Used by Permalink
def search_files(build_type,name):
    ret = None
    path = None
    if build_type == 'n':
        path = FakeDB('static/n').by_name(name)
    elif build_type == 'r':
        path = FakeDB('static/r').by_name(name)
    if path:
        ret = os.path.join('/',path)
    return ret

# Used by Logs
def find_logs(location='static/n'):
    dates = []
    try:
        dirs = os.listdir(location)
    except OSError:
        pass
    for d in dirs:
        if os.path.isdir(os.path.join(location,d)) and d.startswith('20'):
            dates.append(d)
    return sorted(dates, reverse=True)

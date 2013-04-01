# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import os
from devices import device_codename
from fakeDatabase import FakeDB

# Used by Devices
def find_builds(device=None):
    if device:
        nightly = FakeDB('static/n').get_device(device=device)
        release = FakeDB('static/r').get_device(device=device)
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
def search_files(name):
    # Check nightlies first
    path = FakeDB('static/n').by_name(name)
    if path:
        # returned path will be relative, so make it absolute
        return os.path.join('/',path)
    # Releases
    path = FakeDB('static/r').by_name(name)
    if path:
        return os.path.join('/',path)
    return None

# Used by Logs
def find_logs(location='static/n'):
    return sorted(os.listdir(location), reverse=True)

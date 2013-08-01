# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import os
import fakeDatabase
from itertools import chain

__all__ = (
        "find_builds",
        "get_screenshots",
        "locate_file",
        "find_logs",
)


# Used by Devices
def find_builds(device=None):
    if device:
        nightly,release,testing,gapps = fakeDatabase.by_device(device)
        builds = { 'release': release, 'nightly': nightly }
    else:
        builds = { 'release':[],'nightly':[] }
    return builds

# Used by Features
def get_screenshots(location='static/res/img/screenshots'):
    screens = []
    try:
        screens = os.listdir(location)
    except OSError as e:
        pass
    return screens

# Used by Permalink2
def locate_file(name):
    if name.endswith('.zip'):
        path = fakeDatabase.by_name(name)
        if path:
            return os.path.join('/',path)

    for (p,d,files) in chain(os.walk(fakeDatabase.testing_location),
            os.walk(fakeDatabase.release_location),
            os.walk(fakeDatabase.gapps_location),
            os.walk(fakeDatabase.nightly_location)):
        for f in files:
            if name == f:
                return os.path.join('/',p,f)

    return None

# Used by Logs
def find_logs(location=fakeDatabase.nightly_location):
    dates = []
    try:
        dirs = os.listdir(location)
    except OSError:
        pass
    for d in dirs:
        if os.path.isdir(os.path.join(location,d)) and d.startswith('20'):
            dates.append(d)
    return sorted(dates, reverse=True)

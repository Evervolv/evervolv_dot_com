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
def get_screenshots(location='static/img/screenshots'):
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

    for (p,d,files) in chain(os.walk('static/n'),
            os.walk('static/r'),os.walk('static/t'),os.walk('static/g')):
        for f in files:
            if name == f:
                return os.path.join('/',p,f)

    return None

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

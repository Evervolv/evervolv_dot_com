# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import os,json,requests
import fakeDatabase

__all__ = (
        "find_builds",
        "get_screenshots",
        "find_logs",
        "get_default_branch",
)

# Used by Devices
def find_builds(device=None):
    if device:
        nightly,release,testing,gapps = fakeDatabase.by_device(device)
        builds = { 'release': release, 'nightly': nightly, 'testing': testing }
    else:
        builds = { 'release':[],'nightly':[], 'testing':[] }
    return builds

# Used by Features
def get_screenshots(location='static/res/img/screenshots'):
    screens = []
    try:
        screens = os.listdir(location)
    except OSError as e:
        pass
    return screens

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

def get_default_branch():
    request = requests.get("https://api.github.com/repos/Evervolv/android")
    repo_info = json.loads(request.text)
    return repo_info['default_branch']

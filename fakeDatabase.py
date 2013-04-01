# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import os
import json

def find_manifests(location, manifest):
    manifests=[]
    for (path,dirs,files) in os.walk(location):
        for f in files:
            if manifest == f:
                manifests.append(os.path.join(path,f))
    return sorted(manifests, reverse=True)

def read_manifests(manifests):
    info = []
    if manifests:
        for m in manifests:
            entries = []
            try:
                f = open(m)
            except IOError as e:
                continue
            else:
                with f:
                    entries = json.load(f)
                for e in entries:
                    info.append(e)
    return info

def parse_manifest(location,manifest):
    m = os.path.join(location,manifest)
    entries = []
    try:
        f = open(m)
    except IOError as e:
        entries = read_manifests(find_manifests(location,'info.json'))
    else:
        with f:
            entries = json.load(f)
        entries.sort(reverse=True,key=lambda d:d['date'])
    return entries

class FakeDB:
    def __init__(self, location='static/n',manifest='manifest.json'):
        self.entries = parse_manifest(location,manifest)
        self.location = location

    def get_device(self, device=None):
        return [e for e in self.entries if e['device'] == device]

    def get_date(self, date=None):
        return [e for e in self.entries if e['date'] == date]

    def dates(self):
        return sorted(set([e['date'] for e in self.entries]), reverse=True)

    def latest(self):
        l = []
        s = self.dates()
        if s: # protect array out of bounds on null list
            l = [e for e in self.entries if e['date'] == s[0]]
        return sorted(l, key=lambda d: d['device'])

    def by_name(self,name):
        p = None
        for e in self.entries:
            if e['name'] == name:
                p = os.path.join(e['date'],e['name'])
        return p


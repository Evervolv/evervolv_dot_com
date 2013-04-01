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
    '''Parse a parent manifest, containing info on all files below it.

    As fall back we can also read individual manifest inside each directory
    named info.json'''
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
    '''Emulate a nosql db by parsing json manifests

      Files are stored in list form with each entry containing
      a dictionary of the following information:
        'date':    string,
        'device':  string,
        'count':   int,
        'location':string,
        'message': string,
        'md5sum':  string,
        'name':    string,
        'size':    int,
        'type':    string (nightly|release),

    The general directory structure this class is expecting:
      static/
        n/
          manifest.json
          {date}/
            {name}
            {name}
            info.json
        r/
          manifest.json
          {codename}/
            {name}
            {name}
            info.json

    '''
    def __init__(self, location,manifest='manifest.json'):
        self.entries = parse_manifest(location,manifest)
        self.location = location

    def by_device(self, device=None):
        '''return all entries for selected {device}'''
        return [e for e in self.entries if e.get('device') == device]

    def get_date(self, date=None):
        '''return all entries for selected {date}'''
        return [e for e in self.entries if e.get('date') == date]

    def dates(self):
        '''return all {dates} reverse sorted (newest->oldest)'''
        return sorted(set([e.get('date') for e in self.entries]), reverse=True)

    def latest(self):
        '''returns all builds for newest date, sorted by device'''
        l = []
        s = self.dates()
        if s: # protect array out of bounds on null list
            l = [e for e in self.entries if e.get('date') == s[0]]
        return sorted(l, key=lambda d: d.get('device'))

    def by_name(self,name):
        '''returns local path of file specified by {name} assumes all entries
           contain a unique {name}'''
        p = None
        for e in self.entries:
            if e.get('name') == name:
                p = os.path.join(self.location,e.get('location'))
        return p


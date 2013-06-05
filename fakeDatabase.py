# Andrew Sutherland <dr3wsuth3rland@gmail.com>

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
        info.json
    r/
      manifest.json
      {codename}/
        {name}
        info.json

'''

import os
import json
import sys

# Helpers
def find_manifests(location, manifest):
    manifests=[]
    for (path,dirs,files) in os.walk(location):
        for f in files:
            if manifest == f:
                manifests.append(os.path.join(path,f))
    return manifests

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
    print >>sys.stderr, 'reading'
    m = os.path.join(location,manifest)
    entries = []
    try:
        f = open(m)
    except IOError as e:
        entries = read_manifests(find_manifests(location,'info.json'))
    else:
        with f:
            entries = json.load(f)
    return entries

# Globals
ENTRIES = (parse_manifest('static/n','manifest.json'), # Nightlies
        parse_manifest('static/r','manifest.json'))    # Releases


# Methods
def by_device(device=None):
    '''return all ENTRIES for selected {device} reverse sorted by date'''
    return (sorted([e for e in ENTRIES[0] if e.get('device') == device],
                key=lambda d: d.get('date'), reverse=True),
            sorted([e for e in ENTRIES[1] if e.get('device') == device],
                key=lambda d: d.get('date'), reverse=True))
           
def by_date(date=None):
    '''return all ENTRIES for selected {date}, sorted by device'''
    return (sorted([e for e in ENTRIES[0] if e.get('date') == date],
                key=lambda d: d.get('device')),
            sorted([e for e in ENTRIES[1] if e.get('date') == date],
                key=lambda d: d.get('device')))

def dates():
    '''return all {dates} reverse sorted (newest->oldest)'''
    return (sorted(set([e.get('date') for e in ENTRIES[0]]), reverse=True),
            sorted(set([e.get('date') for e in ENTRIES[1]]), reverse=True))

def latest():
    '''returns all builds for newest date, sorted by device'''
    ln = []
    lr = []
    n,r = dates()
    if n: # protect array out of bounds on null list
        ln = by_date(n[0])[0]
    if r:
        lr = by_date(r[0])[1]
    return (ln,lr)

def by_name(name):
    '''returns local path of file specified by {name} assumes all entries
       contain a unique {name}'''
    p = None
    for e in ENTRIES[0]:
        if e.get('name') == name:
            p = os.path.join('static/n',e.get('location'))
    if not p:
        for e in ENTRIES[1]:
            if e.get('name') == name:
                p = os.path.join('static/r',e.get('location'))
    return p



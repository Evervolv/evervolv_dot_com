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
import time

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

def parse_manifest(location,manifest='manifest.json'):
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
    return entries

# Globals
nightly_location = os.path.join('static','n')
release_location = os.path.join('static','r')

manifest_entries = (parse_manifest(nightly_location), # Nightlies
                    parse_manifest(release_location)) # Releases

cache_expiry = time.time() + 300

def entries():
    '''Wrapper for manifest_entries to allow updating cache

    '''
    global manifest_entries
    global cache_expiry
    if time.time() > cache_expiry:
        cache_expiry = time.time() + 300
        manifest_entries = (parse_manifest(nightly_location), # Nightlies
                            parse_manifest(release_location)) # Releases
    return manifest_entries

# Methods
def by_device(device=None):
    '''return all manifest_entries (tuple) for selected {device} reverse sorted by date

    '''
    return (sorted([e for e in entries()[0] if e.get('device') == device],
                key=lambda d: d.get('date'), reverse=True),
            sorted([e for e in entries()[1] if e.get('device') == device],
                key=lambda d: d.get('date'), reverse=True))

def by_date(date=None):
    '''return all manifest_entries (tuple) for selected {date}, sorted by device

    '''
    return (sorted([e for e in entries()[0] if e.get('date') == date],
                key=lambda d: d.get('device')),
            sorted([e for e in entries()[1] if e.get('date') == date],
                key=lambda d: d.get('device')))

def dates():
    '''return all {dates} (tuple) reverse sorted (newest->oldest)

    '''
    return (sorted(set([e.get('date') for e in entries()[0]]), reverse=True),
            sorted(set([e.get('date') for e in entries()[1]]), reverse=True))

def latest():
    '''returns all builds (tuple) for newest date, sorted by device

    '''
    ln = []
    lr = []
    n,r = dates()
    if n: # protect array out of bounds on null list
        ln = by_date(n[0])[0]
    if r:
        lr = by_date(r[0])[1]
    return (ln,lr)

def by_name(name):
    '''returns local path (string) of file specified by {name}

    assumes all entries contain a unique {name}'''
    p = None
    for e in entries()[0]: # Nightlies
        if e.get('name') == name:
            p = os.path.join(nightly_location,e.get('location'))
    if not p:
        for e in entries()[1]: # Releases
            if e.get('name') == name:
                p = os.path.join(release_location,e.get('location'))
    return p

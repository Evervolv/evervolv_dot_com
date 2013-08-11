# The Evervolv Project
import os
import web
import Queue
import threading
import fakeDatabase
from itertools import chain

DATABASE_NAME   = 'downloads.db'
TABLE_NAME      = 'stats'
COLUMN_ID       = "_id"
COLUMN_DATE     = "date"
COLUMN_NAME     = "name"
COLUMN_MD5SUM   = "md5sum"
COLUMN_LOCATION = "location"
COLUMN_DEVICE   = "device"
COLUMN_MESSAGE  = "message"
COLUMN_TYPE     = "type"
COLUMN_SIZE     = "size"
COLUMN_COUNT    = "count"

TABLE_TEMPLATE = " (" + \
    COLUMN_ID  + " INTEGER PRIMARY KEY AUTOINCREMENT, " + \
    COLUMN_DATE     + " TEXT, " + \
    COLUMN_NAME     + " TEXT, " + \
    COLUMN_MD5SUM   + " TEXT, " + \
    COLUMN_LOCATION + " TEXT, " + \
    COLUMN_DEVICE   + " TEXT, " + \
    COLUMN_MESSAGE  + " TEXT, " + \
    COLUMN_TYPE     + " TEXT, " + \
    COLUMN_SIZE     + " INT, " + \
    COLUMN_COUNT    + " INT);"

class dbThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            f = self.q.get()
            try:
                increment(f)
            except:
                pass # What can we do?
            self.q.task_done()

# To init db
if not os.path.exists(DATABASE_NAME):
    import subprocess
    # Create database: Intentionally throw error
    subprocess.check_call(("sqlite3", "-batch", DATABASE_NAME,
        "CREATE TABLE " + TABLE_NAME + TABLE_TEMPLATE
    ))

# Database connection
db = web.database(dbn='sqlite', db=DATABASE_NAME)
# Queue to process db entries
q = Queue.Queue()
# Single thread to process queue
t = dbThread(q)
t.setDaemon(True)
t.start() # Runs indefinitely

# Used by Permalink2
def get(name):
    if name.endswith('.zip'):
        path = fakeDatabase.by_name(name)
        if path is not None:
            q.put(name)
            return os.path.join('/',path)

    for (p,d,files) in chain(os.walk(fakeDatabase.testing_location),
            os.walk(fakeDatabase.release_location),
            os.walk(fakeDatabase.gapps_location),
            os.walk(fakeDatabase.nightly_location)):
        for f in files:
            if name == f:
                q.put(name)
                return os.path.join('/',p,f)
    return None


def select(filename):
    return db.select(TABLE_NAME, vars=locals(), where="%s=$filename" % COLUMN_NAME)

def increment(filename):
    entries = select(filename)
    # Weird hack
    entry = None
    for e in entries:
        entry = e
        break
    if entry is not None: # Update existing
        db.update(TABLE_NAME,
                where="%s=%s" % (COLUMN_ID,entry._id),
                count=entry.count+1)
    else: # Add new
        manifest_entry = fakeDatabase.get_entry(name=filename)
        if manifest_entry is not None: # Info available: add it in
            db.insert(TABLE_NAME,
                    date=manifest_entry.get(COLUMN_DATE),
                    name=manifest_entry.get(COLUMN_NAME),
                    md5sum=manifest_entry.get(COLUMN_MD5SUM),
                    location=manifest_entry.get(COLUMN_LOCATION),
                    device=manifest_entry.get(COLUMN_DEVICE),
                    message=manifest_entry.get(COLUMN_MESSAGE),
                    type=manifest_entry.get(COLUMN_TYPE),
                    size=manifest_entry.get(COLUMN_SIZE),
                    count=1)
        else: # Bare entry: changelogs and such
            db.insert(TABLE_NAME,
                    name=filename,
                    count=1)

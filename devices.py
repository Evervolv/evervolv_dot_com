# The Evervolv Project

# These do not get sorted
# the order here is how they appear on the website
devices = (
    'bravo',
    'd710',
    'gapps',
    'glacier',
    'grouper',
    'inc',
    'jewel',
    'kingdom',
    'mako',
    'manta',
    'passion',
    'ruby',
    'shooter',
    'speedy',
    'supersonic',
    'tenderloin',
    'toro',
    'vivow',
)

# format 'device name': ('codename','retail name')
# the codename is also the directory searched for builds
device_names = {
    'bravo': ('Turba','HTC Desire (GSM)'),
    'd710': ('Clarus','Samsung Epic 4G Touch'),
    'gapps': ('Gapps','Google Apps'),
    'glacier': ('Glacialis','T-mobile myTouch 4G'),
    'grouper': ('Mirus','Google Nexus 7'),
    'inc': ('Dives','HTC Droid Incredible'),
    'jewel': ('Bellus','HTC Evo 4G LTE'),
    'kingdom': ('Scio','HTC Evo Design 4G'),
    'mako': ('Fulsi','Google Nexus 4'),
    'manta': ('Stella','Google Nexus 10'),
    'passion': ('Perdo','Google Nexus One'),
    'ruby': ('Iaceo','HTC Amaze 4G'),
    'shooter': ('Neco','HTC Evo 3D'),
    'speedy': ('Artis','HTC Evo Shift 4G'),
    'supersonic': ('Acies','HTC Evo 4G'),
    'tenderloin': ('Queo','HP Touchpad'),
    'toro': ('Primo','Samsung Galaxy Nexus (VZW)'),
    'vivow': ('Conor','HTC Droid Incredible 2'),
}

def device_codename(device):
    return device_names[device][0]

def device_retail_name(device):
    return device_names[device][1]

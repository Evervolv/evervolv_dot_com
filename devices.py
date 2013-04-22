# The Evervolv Project

# XXX: EDITING :XXX
# ADDING DEVICES:
#     Add to the devices tuple, should be alphabetical.
#     Add to device_info dictionary, fill out all fields
# ADDING MAINTAINERS:
#     Add yourself to the bottom of the maintainers tuple.
#     Add yourself to maintainers_info dictionary, url should be twitter or
#       g+ (somewhere you publicly post your android news) 

__all__ = (
    'devices',
    'maintainers',
    'maintainer_info',
    'device_codename',
    'device_retail_name',
    'device_maintainer',
    'maintainer_devices',
)

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
    'pyramid',
    'ruby',
    'shooter',
    'speedy',
    'supersonic',
    'tenderloin',
    'vivow',
)

device_info = {
    'bravo': {
        'codename': 'Turba',
        'retail_name': 'HTC Desire (GSM)',
        'maintainer': 'Nikez',
    },
    'd710': {
        'codename': 'Clarus',
        'retail_name': 'Samsung Epic 4G Touch',
        'maintainer': '',
    },
    'gapps': {
        'codename': 'Gapps',
        'retail_name': 'Google Apps',
        'maintainer': '',
    },
    'glacier': {
        'codename': 'Glacialis',
        'retail_name': 'T-mobile myTouch 4G',
        'maintainer': 'elginsk8r',
    },
    'grouper': {
        'codename': 'Mirus',
        'retail_name': 'Google Nexus 7',
        'maintainer': 'drewis',
    },
    'inc': {
        'codename': 'Dives',
        'retail_name': 'HTC Droid Incredible',
        'maintainer': '',
    },
    'jewel': {
        'codename': 'Bellus',
        'retail_name': 'HTC Evo 4G LTE',
        'maintainer': 'preludedrew',
    },
    'kingdom': {
        'codename': 'Scio',
        'retail_name': 'HTC Evo Design 4G',
        'maintainer': 'preludedrew',
    },
    'mako': {
        'codename': 'Fulsi',
        'retail_name': 'Google Nexus 4',
        'maintainer': 'drewis',
    },
    'manta': {
        'codename': 'Stella',
        'retail_name': 'Google Nexus 10',
        'maintainer': '',
    },
    'passion': {
        'codename': 'Perdo',
        'retail_name': 'Google Nexus One',
        'maintainer': 'drewis',
    },
    'pyramid': {
        'codename': 'Macto',
        'retail_name': 'HTC Sensation',
        'maintainer': 'Nikez',
    },
    'ruby': {
        'codename': 'Iaceo',
        'retail_name': 'HTC Amaze 4G',
        'maintainer': 'preludedrew',
    },
    'shooter': {
        'codename': 'Neco',
        'retail_name': 'HTC Evo 3D',
        'maintainer': 'preludedrew',
    },
    'speedy': {
        'codename': 'Artis',
        'retail_name': 'HTC Evo Shift 4G',
        'maintainer': 'preludedrew',
    },
    'supersonic': {
        'codename': 'Acies',
        'retail_name': 'HTC Evo 4G',
        'maintainer': 'preludedrew',
    },
    'tenderloin': {
        'codename': 'Queo',
        'retail_name': 'HP Touchpad',
        'maintainer': 'preludedrew',
    },
    'vivow': {
        'codename': 'Conor',
        'retail_name': 'HTC Droid Incredible 2',
        'maintainer': 'preludedrew',
    },
}

maintainers = (
    'preludedrew',
    'drewis',
    'Nikez',
    'elginsk8r',
)

maintainer_info = {
    'preludedrew': {
        'url': 'http://twitter.com/preludedrew',
        'extra': ('Founder',),
    },
    'drewis': {
        'url': 'https://plus.google.com/u/0/102710594547223731659/posts',
        'extra': ('Site Admin',),
    },
    'Nikez': {
        'url': 'http://twitter.com/LaidbackNikez',
    },
    'elginsk8r': {
        'url': 'https://plus.google.com/u/0/100948280470840956633/posts',
    },
}

def device_codename(device):
    return device_info.get(device).get('codename')

def device_retail_name(device):
    return device_info.get(device).get('retail_name')

def device_maintainer(device):
    return device_info.get(device).get('maintainer')

def maintainer_devices(name):
    return [ d for d in devices if device_maintainer(d) == name ]

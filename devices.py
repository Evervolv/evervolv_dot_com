# The Evervolv Project

# XXX: EDITING :XXX
# ADDING DEVICES:
#     Add to the devices tuple, should be alphabetical.
#     'maintainer' field needs to be a tuple, so single entries need a trailing comma
# ADDING MAINTAINERS:
#     Add yourself to the bottom of the maintainers tuple,
#     'url' should be twitter or g+ (somewhere you publicly post your android news) 

__all__ = (
    'devices',
    'maintainers',
    'device_info',
    'maintainer_info',
)

# These do not get sorted
# the order here is how they appear on the website

devices = (
    {
        'device': 'bravo',
        'codename': 'Turba',
        'retail_name': 'HTC Desire (GSM)',
        'maintainer': ('Nikez',),
    },
    {
        'device': 'd710',
        'codename': 'Clarus',
        'retail_name': 'Samsung Epic 4G Touch',
        'maintainer': ('Dastin',),
    },
    {
        'device': 'gapps',
        'codename': 'Gapps',
        'retail_name': 'Google Apps',
        'maintainer': ('',),
    },
    {
        'device': 'glacier',
        'codename': 'Glacialis',
        'retail_name': 'T-mobile myTouch 4G',
        'maintainer': ('elginsk8r',),
    },
    {
        'device': 'grouper',
        'codename': 'Mirus',
        'retail_name': 'Google Nexus 7',
        'maintainer': ('drewis',),
    },
    {
        'device': 'inc',
        'codename': 'Dives',
        'retail_name': 'HTC Droid Incredible',
        'maintainer': ('',),
    },
    {
        'device': 'jewel',
        'codename': 'Bellus',
        'retail_name': 'HTC Evo 4G LTE',
        'maintainer': ('preludedrew',),
    },
    {
        'device': 'kingdom',
        'codename': 'Scio',
        'retail_name': 'HTC Evo Design 4G',
        'maintainer': ('preludedrew',),
    },
    {
        'device': 'mako',
        'codename': 'Fulsi',
        'retail_name': 'Google Nexus 4',
        'maintainer': ('drewis',),
    },
    {
        'device': 'manta',
        'codename': 'Stella',
        'retail_name': 'Google Nexus 10',
        'maintainer': ('',),
    },
    {
        'device': 'passion',
        'codename': 'Perdo',
        'retail_name': 'Google Nexus One',
        'maintainer': ('drewis',),
    },
    {
        'device': 'pyramid',
        'codename': 'Macto',
        'retail_name': 'HTC Sensation',
        'maintainer': ('Nikez',),
    },
    {
        'device': 'ruby',
        'codename': 'Iaceo',
        'retail_name': 'HTC Amaze 4G',
        'maintainer': ('preludedrew',),
    },
    {
        'device': 'shooter',
        'codename': 'Neco',
        'retail_name': 'HTC Evo 3D',
        'maintainer': ('preludedrew','Flintman','Dastin'),
    },
    {
        'device': 'speedy',
        'codename': 'Artis',
        'retail_name': 'HTC Evo Shift 4G',
        'maintainer': ('preludedrew','Dastin'),
    },
    {
        'device': 'supersonic',
        'codename': 'Acies',
        'retail_name': 'HTC Evo 4G',
        'maintainer': ('preludedrew',),
    },
    {
        'device': 'tenderloin',
        'codename': 'Queo',
        'retail_name': 'HP Touchpad',
        'maintainer': ('preludedrew','Flintman'),
    },
    {
        'device': 'vivow',
        'codename': 'Conor',
        'retail_name': 'HTC Droid Incredible 2',
        'maintainer': ('preludedrew',),
    },
)

maintainers = (
    {
        'name': 'preludedrew',
        'url': 'http://twitter.com/preludedrew',
        'extra': ('Founder','Admin'),
    },
    {
        'name': 'drewis',
        'url': 'https://plus.google.com/u/0/102710594547223731659/posts',
        'extra': ('Admin',),
    },
    {
        'name': 'Nikez',
        'url': 'http://twitter.com/LaidbackNikez',
    },
    {
        'name': 'elginsk8r',
        'url': 'https://plus.google.com/u/0/100948280470840956633/posts',
    },
    {
        'name': 'Flintman',
        'url': 'http://twitter.com/wbellavance',
    },
    {
        'name': 'Dastin',
        'url': 'http://twitter.com/dastin1015',
    },
)

def device_info(device):
    for d in devices:
        if d.get('device') == device:
            return d
    return {}

def maintainer_info(name):
    info = {}
    for m in maintainers:
        if m.get('name') == name:
            info = m
            info['devices'] = tuple(d.get('device') for d in devices if name in
                    device_info(d.get('device')).get('maintainer'))
    return info

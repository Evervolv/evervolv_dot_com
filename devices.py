# The Evervolv Project

# XXX: EDITING :XXX
# ADDING DEVICES:
#     Add to the devices tuple, should be alphabetical.
# ADDING MAINTAINERS:
#     Add yourself to the bottom of the maintainers tuple,
#     url should be twitter or g+ (somewhere you publicly post your android news) 

__all__ = (
    'devices',
    'maintainers',
)

# These do not get sorted
# the order here is how they appear on the website

devices = {
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
    'preludedrew': {
        'url': 'http://twitter.com/preludedrew',
        'extra': ('Founder','Admin'),
        },
    'drewis': {
        'url': 'https://plus.google.com/u/0/102710594547223731659/posts',
        'extra': ('Admin',),
    },
    'Nikez': {
        'url': 'http://twitter.com/LaidbackNikez',
    },
    'elginsk8r': {
        'url': 'https://plus.google.com/u/0/100948280470840956633/posts',
    },
)

# Add devices to maintainers tuple
for m in maintainers.keys():
    maintainers[m]['devices'] = tuple(d for d in devices.keys() if
                    devices.get(d).get('maintainer') == m)

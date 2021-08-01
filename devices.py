# The Evervolv Project

# XXX: EDITING :XXX
# ADDING DEVICES:
#     Add to the _devices dict, should be alphabetical.
#     'maintainer' field needs to be a tuple, so single entries need a trailing comma
# ADDING MAINTAINERS:
#     Add yourself to the bottom of the _maintainers dict,
#     'url' should be twitter or g+ (somewhere you publicly post your android news) 


from collections import OrderedDict

__all__ = (
    'devices',
    'maintainers',
)

_devices = {
    'bravo': {
        'codename': 'Turba',
        'retail_name': 'HTC Desire (GSM)',
        'maintainer': ('Nikez',),
        'legacy': True,
    },
    'celox': {
        'codename': 'Potens',
        'retail_name': 'Samsung Galaxy S II (AT&T/T-Mobile)',
        'maintainer': ('elginsk8r',),
        'legacy': True,
    },
    'flo': {
        'codename': 'Ferus',
        'retail_name': 'Google Nexus 7 (2013)',
        'maintainer': ('elginsk8r',),
    },
    'glacier': {
        'codename': 'Glacialis',
        'retail_name': 'T-mobile myTouch 4G',
        'maintainer': ('elginsk8r',),
        'legacy': True,
    },
    'grouper': {
        'codename': 'Mirus',
        'retail_name': 'Google Nexus 7 (2012)',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
    'gt58wifi': {
        'codename': 'Sedo',
        'retail_name': 'Samsung Galaxy Tab A 8.0 (Wifi)',
        'maintainer': ('elginsk8r',),
    },
    'guacamole': {
        'codename': 'Expletus',
        'retail_name': 'OnePlus OnePlus7 Pro',
        'maintainer': ('elginsk8r',),
    },
    'hammerhead': {
        'codename': 'Pugno',
        'retail_name': 'Google Nexus 5',
        'maintainer': ('preludedrew','elginsk8r'),
    },
    'inc': {
        'codename': 'Dives',
        'retail_name': 'HTC Droid Incredible',
        'maintainer': ('MongooseHelix',),
        'legacy': True,
    },
    'jewel': {
        'codename': 'Bellus',
        'retail_name': 'HTC Evo 4G LTE',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
    'jfltevzw': {
        'codename': 'Fruor',
        'retail_name': 'Samsung Galaxy S4 (Verizon)',
        'maintainer': ('Flintman',),
        'legacy': True,
    },
    'kingdom': {
        'codename': 'Scio',
        'retail_name': 'HTC Evo Design 4G',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
    'm7spr': {
        'codename': 'Regius',
        'retail_name': 'HTC One (Sprint)',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
    'mako': {
        'codename': 'Fulsi',
        'retail_name': 'Google Nexus 4',
        'maintainer': ('drewis',),
        'legacy': True,
    },
    'manta': {
        'codename': 'Stella',
        'retail_name': 'Google Nexus 10',
        'maintainer': ('',),
        'legacy': True,
    },
    'oneplus3': {
        'codename': 'Plures',
        'retail_name': 'OnePlus OnePlus3',
        'maintainer': ('elginsk8r'),
    },
    'passion': {
        'codename': 'Perdo',
        'retail_name': 'Google Nexus One',
        'maintainer': ('drewis',),
        'legacy': True,
    },
    'potter': {
        'codename': 'Motus',
        'retail_name': 'Motorola G5 Plus',
        'maintainer': ('Flintman',),
        'legacy': True,
    },
    'pyramid': {
        'codename': 'Macto',
        'retail_name': 'HTC Sensation',
        'maintainer': ('Nikez',),
        'legacy': True,
    },
    'ruby': {
        'codename': 'Iaceo',
        'retail_name': 'HTC Amaze 4G',
        'maintainer': ('preludedrew','jeepers007'),
        'legacy': True,
    },
    'shamu': {
        'codename': 'Immanis',
        'retail_name': 'Motorola Nexus 6',
        'maintainer': ('elginsk8r',),
    },
    'shooter': {
        'codename': 'Neco',
        'retail_name': 'HTC Evo 3D',
        'maintainer': ('preludedrew','Flintman'),
        'legacy': True,
    },
    'soho': {
        'codename': 'lectio',
        'retail_name': 'Kindle Fire HD 3rd Generation',
        'maintainer': ('Flintman'),
        'legacy': True,
    },
    'speedy': {
        'codename': 'Artis',
        'retail_name': 'HTC Evo Shift 4G',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
    'supersonic': {
        'codename': 'Acies',
        'retail_name': 'HTC Evo 4G',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
    'tenderloin': {
        'codename': 'Queo',
        'retail_name': 'HP Touchpad',
        'maintainer': ('preludedrew','Flintman','elginsk8r'),
        'legacy': True,
    },
    'tenderloin4g': {
        'codename': 'Quae',
        'retail_name': 'HP Touchpad 4G',
        'maintainer': ('Flintman'),
        'legacy': True,
    },
    'toro': {
        'codename': 'Primo',
        'retail_name': 'Samsung Galaxy Nexus (Verizon)',
        'maintainer': ('MongooseHelix',),
        'legacy': True,
    },
    'vivow': {
        'codename': 'Conor',
        'retail_name': 'HTC Droid Incredible 2',
        'maintainer': ('preludedrew',),
        'legacy': True,
    },
}

# Note: this is initialized as a list of tuples
# This will not get sorted, order here is how it appears on the site
_maintainers = OrderedDict ([
    (
        'preludedrew',
        {
            'url': 'http://twitter.com/preludedrew',
            'extra': ('Founder','Admin','Inactive',),
        }
    ),
    (
        'drewis',
        {
            'url': 'https://github.com/drewis',
            'extra': ('Admin','Inactive',),
        }
    ),
    (
        'MongooseHelix',
        {
            'url': 'http://twitter.com/MongooseHelix',
            'extra': ('Admin','Inactive',),
        }
    ),
    (
        'elginsk8r',
        {
            'url': 'https://github.com/elginsk8r',
            'extra': ('Admin',),
        }
    ),
    (
        'Flintman',
        {
            'url': 'http://twitter.com/wbellavance',
            'extra': ('Admin',),
        }
    ),
    (
        'Nikez',
        {
            'url': 'http://twitter.com/LaidbackNikez',
            'extra': ('Inactive',),
        }
    ),
    (
        'jeepers007',
        {
            'url': 'http://forum.xda-developers.com/member.php?u=693610',
            'extra': ('Inactive',),
        }
    ),
])

# Add devices to _maintainers
for m in _maintainers.keys():
    _maintainers[m]['devices'] = tuple(sorted(d for d in _devices.keys() if m in
                    _devices.get(d).get('maintainer')))

# Public
def devices(device=None):
    if device:
        return _devices.get(device)
    else:
        return sorted(_devices.keys())

def maintainers(name=None):
    if name:
        return _maintainers.get(name)
    else:
        return _maintainers.keys()

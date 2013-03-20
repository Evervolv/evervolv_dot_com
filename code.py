#!/usr/bin/env python2
# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import web
import os

# apache hax for local imports
#import os, sys
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)
# local imports
from devices import device_retail_name, device_codename, devices

urls = (
    '/','Default',
    '/about/', 'About',
    '/chat/', 'Chat',
    '/devices/(.*)', 'Devices',
    '/news/', 'News',
    '/source/', 'Source',
    '/features/', 'Features',
    # Redirects for manually typed addresses
    '/([Aa]bout|[Cc]hat|[Dd]evices|[Nn]ews|[Ss]ource|[Ff]eatures)', 'AddSlash',
    '/[Dd]ownloads?', 'SeeDevices',
    # Other
    '/robots.txt', 'Robots',
    # Catchall
    '/.*', 'SeeDefault',
)

t_globals = {
    'device_retail_name': device_retail_name,
    'device_codename': device_codename,
    'devices': devices,
}

render = web.template.render('template', base='base',globals=t_globals)

class Default:
    def GET(self):
        return render.default()

class About:
    def GET(self):
        return render.about()

class Chat:
    def GET(self):
        return render.chat()

class Devices:
    def GET(self,device=None):
        #placeholder
        files={
        'release': [{'name':'Evervolv-Fulsi-3.2.0p2-mako.zip'},{'name': 'Evervolv-Fulsi-3.2.0p1-mako.zip'},{'name':'Evervolv-Fulsi-3.2.0p0-mako.zip'}],
        'nightly': [{'name':'Evervolv-Fulsi-3.2.0-Nightly-2013.03.12-mako.zip','date':'2013.03.12','md5sum':'ed466d0dfb26f79cf4ebb4e09059bf46','size':300000000},{'name':'Evervolv-Fulsi-3.2.0-Nightly-2013.03.10-mako.zip','date':'2013.03.10','md5sum':'ed466d0dfb26f79cf4ebb4e09059bf46','size':300000000},{'name':'Evervolv-Fulsi-3.2.0-Nightly-2013.03.05-mako.zip','date':'2013.03.05','md5sum':'ed466d0dfb26f79cf4ebb4e09059bf46','size':300000000}]
        }
        if device:
            return render.builds(device,files)
        return render.devices()

class News:
    def GET(self):
        return render.news()

class Source:
    def GET(self):
        return render.source()

class Features:
    def GET(self):
        screenshots = os.listdir('static/img/screenshots/')
        return render.features(screenshots)

class AddSlash:
    def GET(self, page):
        raise web.seeother('/%s/' % page.lower())

class SeeDevices:
    def GET(self):
        raise web.seeother('/devices/')

class Robots:
    def GET(self):
        return 'User-agent: *\nDisallow: /static/'

class SeeDefault:
    def GET(self):
        raise web.seeother('/')

# lighttpd
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# apache2 + wsgi
#application = web.application(urls, globals()).wsgifunc()

#!/usr/bin/env python2
# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import web
import os

if __name__ != "__main__":              # mod_wsgi has no concept of where it is
    os.chdir(os.path.dirname(__file__)) # any relative paths will fail without this

# local imports
from devices import *
from operations import *
from sitemap import Sitemap
import api

urls = (
    '/','Default',
    '/about/', 'About',
    '/chat/', 'Chat',
    '/devices/(.*)/', 'Devices',
    '/devices/(.*)', 'Devices',
#    '/news/', 'News',
    '/source/', 'Source',
    '/features/', 'Features',
    # Redirects for manually typed addresses
    # The idea here is to force any variations to the above paths
    '/([Aa]bout|[Cc]hat|[Dd]evices)', 'AddSlash',
    '/([Nn]ews|[Ss]ource|[Ff]eatures)', 'AddSlash',
    '/[Dd]ownloads?', 'SeeDevices',
    # Other
    '/robots.txt', 'Robots',
    '/sitemap.xml', 'SiteMap',
    '/get/(r|n)/(.+)', 'Permalink',
    '/get/(.+)', 'Permalink2',
    '/logs?', 'Logs',
    '/api/v(\d+)/(.+)/(.+)/(.+)','ApiHandler',
    # Error
    '/404/', 'NotFound',
    # Catchall
    '/(.+)', 'Catchall',
)

t_globals = {
    'devices': devices,
    'maintainers': maintainers,
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
        if device:
            if device not in devices():
                raise web.seeother('/404/')
            return render.builds(device,find_builds(device))
        return render.devices()

class News:
    def GET(self):
        return render.news()

class Source:
    def GET(self):
        return render.source()

class Features:
    def GET(self):
        return render.features(get_screenshots())

class AddSlash:
    def GET(self, page):
        raise web.seeother('/%s/' % page.lower())

class SeeDevices:
    def GET(self):
        raise web.seeother('/devices/')

class Robots:
    def GET(self):
        return 'User-agent: *\nDisallow: /static/\nSitemap: http://evervolv.com/sitemap.xml'

class SiteMap:
    def GET(self):
        m = Sitemap()
        m.add_url('http://evervolv.com',priority='1.0')
        m.add_url('http://evervolv.com/about/',priority='0.8')
        m.add_url('http://evervolv.com/chat/',priority='0.3')
        m.add_url('http://evervolv.com/devices/',priority='0.8')
        m.add_url('http://evervolv.com/news/',priority='0.3')
        m.add_url('http://evervolv.com/source/',priority='0.6')
        m.add_url('http://evervolv.com/features/',priority='0.6')
        for d in devices():
            m.add_url('http://evervolv.com/devices/%s' % d,
                    changefreq='daily',priority='0.1')
        return m.write()

class Permalink: # Depreciated: don't care about build type
    def GET(self,build_type=None,f=None):
        if f is not None:
            path = locate_file(f)
            if path:
                raise web.seeother(path)
        raise web.notfound()

class Permalink2:
    def GET(self,f=None):
        if f is not None:
            path = locate_file(f)
            if path:
                raise web.seeother(path)
        raise web.notfound()

class Logs:
    def GET(self):
        return render.logs(find_logs())

class ApiHandler:
    def GET(self,version=None,action=None,build_type=None,device=None):
        ret = None
        if version and build_type and action and device:
            if int(version) == 1:
                ret = api.v1_perform(action,build_type,device)
        if not ret:
            raise web.notfound()
        return ret

class NotFound:
    def GET(self):
        return render.error()

class Catchall:
    def GET(self,path=None):
        raise web.seeother('/404/')

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run() # devel
else:
    application = app.wsgifunc() # apache2 + wsgi

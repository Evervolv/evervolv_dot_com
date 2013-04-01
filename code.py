#!/usr/bin/env python2
# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import web

# apache hax for local imports
#import os, sys
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)
# local imports
from devices import device_retail_name, device_codename, devices
from operations import find_builds, get_screenshots, search_files, find_logs
from sitemap import Sitemap

urls = (
    '/','Default',
    '/about/', 'About',
    '/chat/', 'Chat',
    '/devices/(.*)', 'Devices',
    '/get/(.*)', 'Permalink',
    '/news/', 'News',
    '/source/', 'Source',
    '/features/', 'Features',
    # Redirects for manually typed addresses
    '/([Aa]bout|[Cc]hat|[Dd]evices|[Nn]ews|[Ss]ource|[Ff]eatures)', 'AddSlash',
    '/[Dd]ownloads?', 'SeeDevices',
    # Other
    '/robots.txt', 'Robots',
    '/sitemap.xml', 'SiteMap',
    '/logs?', 'Logs',
    # Error
    '/404/', 'NotFound',
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
        if device:
            return render.builds(device,find_builds(device))
        return render.devices()

class Permalink:
    def GET(self,f=None):
        if f and f.endswith('.zip'):
            path = search_files(f)
            if path:
                raise web.seeother(path)
        raise web.seeother('/404/')

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
        for d in devices:
            m.add_url('http://evervolv.com/devices/%s' % d,
                    changefreq='daily',priority='0.1')
        return m.write()

class Logs:
    def GET(self):
        return render.logs(find_logs())

class NotFound:
    def GET(self):
        return '404' #FIXME

class SeeDefault:
    def GET(self):
        raise web.seeother('/')

# lighttpd
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# apache2 + wsgi
#application = web.application(urls, globals()).wsgifunc()

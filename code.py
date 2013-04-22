#!/usr/bin/env python2
# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import web

# apache hax for local imports
#import os, sys
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)
# local imports
from devices import *
from operations import find_builds, get_screenshots, search_files, find_logs
from sitemap import Sitemap
import api

urls = (
    '/','Default',
    '/about/', 'About',
    '/chat/', 'Chat',
    '/devices/(.*)', 'Devices',
    '/news/', 'News',
    '/source/', 'Source',
    '/bugs','Bugs',
    '/features/', 'Features',
    # Redirects for manually typed addresses
    # The idea here is to force any variations to the above paths
    '/([Aa]bout|[Cc]hat|[Dd]evices)', 'AddSlash',
    '/([Nn]ews|[Ss]ource|[Ff]eatures)', 'AddSlash',
    '/[Dd]ownloads?', 'SeeDevices',
    '/[Bb]ugs','Bugs',
    # Other
    '/robots.txt', 'Robots',
    '/sitemap.xml', 'SiteMap',
    '/get/(r|n)/(.+)', 'Permalink',
    '/logs?', 'Logs',
    '/api/v(\d+)/(r|n)/(.+)/(.+)','ApiHandler',
    # Error
    '/404/', 'NotFound',
    # Catchall
    '/(.+)', 'Catchall',
)

t_globals = {
    'devices': devices,
    'maintainers': maintainers,
    'maintainer_info': maintainer_info,
    'device_codename': device_codename,
    'device_retail_name': device_retail_name,
    'device_maintainer': device_maintainer,
    'maintainer_devices': maintainer_devices,
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

class News:
    def GET(self):
        return render.news()

class Source:
    def GET(self):
        return render.source()
class Bugs:
    def GET(self):
        raise web.seeother('http://bugs.evervolv.com')
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

class Permalink:
    def GET(self,build_type=None,f=None):
        if build_type and f and f.endswith('.zip'):
            path = search_files(build_type,f)
            if path:
                raise web.seeother(path)
        raise web.seeother('/404/')

class Logs:
    def GET(self):
        return render.logs(find_logs())

class ApiHandler:
    def GET(self,version=None,build_type=None,action=None,item=None):
        ret = ''
        if version and action and build_type and item:
            if int(version) == 1:
              if action == 'get':
                  raise web.seeother('/get/%s/%s' % (build_type,item))
              else:
                  return api.v1_perform(action,build_type,item)
            else:
              pass
        else:
            pass
        return ret

class NotFound:
    def GET(self):
        return render.error()

class Catchall:
    def GET(self,path=None):
        raise web.seeother('/404/')

# lighttpd
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# apache2 + wsgi
#application = web.application(urls, globals()).wsgifunc()

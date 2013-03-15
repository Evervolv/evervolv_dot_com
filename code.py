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

urls = (
    '/','Default',
    '/[Dd]evice.*/(.*)', 'Devices',
    '/robots.txt', 'Robots',
    '/.*', 'Redirect',
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

class Devices:
    def GET(self,device=None,files=None):
        #temp
        files=['Sample','sample2']
        return render.devices(device,files)

class Robots:
    def GET(self):
        return 'User-agent: *\nDisallow: /static/'

class Redirect:
    def GET(self):
        raise web.seeother('/')

# lighttpd
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# apache2 + wsgi
#application = web.application(urls, globals()).wsgifunc()

#!/usr/bin/env python2
# Andrew Sutherland <dr3wsuth3rland@gmail.com>
import web


# apache hax for local imports
#import os, sys
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)


urls = (
    '/','Default',
    '/robots.txt', 'Robots',
    '/.*', 'Redirect',
)

render = web.template.render('template', base='base')

class Default:
    def GET(self):
        return render.default()

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

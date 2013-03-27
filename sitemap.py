# Andrew Sutherland <dr3wsuth3rland@gmail.com>
# Genarate a site map ondemand

class Sitemap(object):
    '''Creates a basic sitemap'''

    def __init__(self):
        self.text = ['<?xml version="1.0" encoding="UTF-8"?>',
                    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                    '</urlset>']

    def add_url(self, url, changefreq=None, priority=None):
        '''takes strings'''
        i = self.text.index('</urlset>')
        self.text.insert(i, '</url>')
        if changefreq:
            self.text.insert(i, '<changefreq>%s</changefreq>' % changefreq)
        if priority:
            self.text.insert(i, '<priority>%s</priority>' % priority)
        self.text.insert(i, '<loc>%s</loc>' % url)
        self.text.insert(i, '<url>')

    def write(self):
        data = ''
        for entry in self.text:
            data += '%s\n' % entry
        return data

#Evervolv.com

##This site is built on [web.py](http://webpy.org/)

####For development

Install ```python-webpy``` (```python2-webpy``` on ARCH)
Then run ```./code.py``` and visit [localhost:8080](http://localhost:8080)

####For deploy

######apache2 + wsgi on ubuntu:

* Install ```python-webpy libapache2-mod-wsgi```
* Setup a new user for the site.
* Clone this repo into ```~/website``` (or where ever).
* Add a new site to apache

To enable webpy under wsgi for the new user:

    WSGIScriptAlias / /<path_to_site>/website/code.py/
    AddType text/html .py
    Alias /static /<path_to_site>/website/static/
    WSGIDaemonProcess <username> user=<username> group=<groupname> python-path=/<path_to_site>/website
    WSGIProcessGroup <username>

Take special note of the ```python-path``` argument, without it wsgi will not find any local imports

When changes are made to the repo they will not show up on the site until the wsgi daemon is restarted, do do so run:

    ./deploy/update.sh

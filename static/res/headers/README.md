#Custom Evervolv directory listings

###To enable:
######Enable the SSI module:
    a2enmod include
######Add the "Includes" option to the directory element:
    <Directory /var/www/>
        Options Indexes FollowSymLinks MultiViews Includes
        AllowOverride None
        Order allow,deny
        allow from all
    </Directory>
######Set path appropriately:
    <IfModule mod_autoindex.c>
        IndexOptions FancyIndexing IgnoreCase VersionSort SuppressHTMLPreamble
        HeaderName /webdata/header.shtml
        ReadmeName /webdata/footer.shtml
        Alias /webdata /var/www/custom
    </IfModule>
######Restart apache:
    service apache2 restart

#!/bin/bash

git clone https://github.com/magic-archive/$1 /public_html

cd /public_html
cp -r * /var/www/html/

cd /var/www/html
chmod 755 -R *

service apache2 restart

tail -f /dev/null

#!/bin/bash
set -e

SERVER_NAME=${SERVER_NAME:-""}
DOCUMENTROOT=${DOCUMENTROOT:-""}



echo"
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        ServerName  $SERVER_NAME
        Alias / /var/www/html/$DOCUMENTROOT/
        <Directory /var/www/html/$DOCUMENTROOT/>
                Options Indexes
#                AllowOverride None
#                Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
" > /etc/apache/sites-available/www.conf

a2ensite www.conf
a2dissite 000-default.conf
exec



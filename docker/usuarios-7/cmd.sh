#!/bin/bash
set -e

SERVER_NAME=${SERVER_NAME:-""}
DOCUMENTROOT=${DOCUMENTROOT:-""}



echo "
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        ServerName  dit.$SERVER_NAME.org
        Alias / /var/www/html/$DOCUMENTROOT/
        <Directory /var/www/html/$DOCUMENTROOT/>
                Options Indexes
#                AllowOverride None
#                Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
" > /etc/apache2/sites-available/000-default.conf

if [[ $VAR != "" ]] ;then
	cp /wordpress /var/www/html/$DOCUMENTROOT/
	chown www-data:www-data -R /var/www/html/$DOCUMENTROOT/wordpress
fi

exec /usr/sbin/apache2 -D FOREGROUND

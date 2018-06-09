FROM danibascon/phpmyadmin

#RUN apt update
#RUN apt install nano php5 libapache2-mod-php5 php5 php5-mysql phpmyadmin -y
RUN ln -s /usr/share/phpmyadmin /var/www/html/
ADD www.conf /etc/apache2/sites-available/
RUN a2ensite www.conf && a2dissite 000-default.conf
ADD config-db.php /etc/phpmyadmin/config-db.php

CMD apachectl -D FOREGROUND


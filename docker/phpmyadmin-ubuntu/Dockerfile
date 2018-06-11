FROM danibascon/phpmyadmin7-ubuntu:1
#FROM ubuntu:16.04

#RUN apt install nano apache2 php7.0 libapache2-mod-php7.0  php7.0-mysql phpmyadmin unzip wget -y

ADD www.conf /etc/apache2/sites-available/www.conf
RUN ln -s /usr/share/phpmyadmin /var/www/html/
RUN a2ensite www.conf && a2dissite 000-default.conf

CMD apachectl -D FOREGROUND







FROM debian:jessie


# Install dependencies.
RUN apt update 
RUN apt install  apache2 libapache2-mod-php5 nano python php5 -y
#RUN apt install php5

# # Install net2ftp.

ADD www.conf /etc/apache2/sites-available/
#ADD usuario.conf /etc/apache2/sites-available/
RUN a2ensite www.conf && a2dissite 000-default.conf

VOLUME /var/wwww/html

RUN mkdir /var/www/html/net2ftp
ADD net2ftp /var/www/html/net2ftp
RUN chmod 0777 /var/www/html/net2ftp/files_to_upload/temp
RUN rm -r /var/www/html/index.html

CMD apachectl -D FOREGROUND


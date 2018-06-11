FROM debian


# Install dependencies.
RUN apt update 
RUN apt install  apache2 libapache2-mod-php7.0 nano python php7.0 php7.0-mysql  -y

VOLUME /var/www/html

#Variables de entorno
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

ADD cmd.sh /cmd.sh
RUN chmod +x /cmd.sh
ADD wordpress /wordpress
EXPOSE 80
CMD ["/cmd.sh"]

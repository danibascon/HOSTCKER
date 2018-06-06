FROM debian:jessie


# Install dependencies.
RUN apt update 
RUN apt install  apache2 libapache2-mod-php5 nano python php5 -y
#RUN apt install php5

# # Install net2ftp.

VOLUME /var/wwww/html
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

ADD cmd.sh /cmd.sh
RUN chmod +x /cmd.sh

EXPOSE 80
CMD ["/cmd.sh"]
#ENTRYPOINT /cmd.sh
#CMD apachectl -D FOREGROUND

#ENTRYPOINT /cmd.sh


FROM debian:jessie


# Install dependencies.
RUN apt update 
RUN apt install  apache2 libapache2-mod-php5 nano python php5 -y
#RUN apt install php5

# # Install net2ftp.

VOLUME /var/wwww/html

ADD cmd.sh /cmd.sh
RUN chmod +x /cmd.sh

EXPOSE 80
CMD ["/cmd.sh"]
#CMD apachectl -D FOREGROUND


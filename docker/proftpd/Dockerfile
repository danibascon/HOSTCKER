FROM proftpd

#RUN apt install  apache2 libapache2-mod-php5 nano python -y
RUN apt install nano python -y

ADD proftpd.conf /etc/proftpd/proftpd.conf
ADD cmd.sh /cmd.sh
ADD usuario.py /usuario.py
RUN chmod +x /cmd.sh
VOLUME /var/www/html

EXPOSE 21
EXPOSE 22

ENTRYPOINT /cmd.sh
#CMD ["proftpd","--nodaemon"]

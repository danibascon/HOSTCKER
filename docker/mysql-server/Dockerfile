FROM danibascon/mysql-server

#RUN apt update
#RUN apt install nano mysql-server -y
RUN apt install python -y

EXPOSE  3306
VOLUME /var/lib/mysql
#ADD cmd.sh /cmd.sh
#ADD mysql.py /mysql.py
#RUN chmod +x /cmd.sh

#ENTRYPOINT /cmd.sh
CMD usr/sbin/mysqld

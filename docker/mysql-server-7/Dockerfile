FROM debian

RUN apt update
RUN apt install nano mysql-server -y

EXPOSE  3306
VOLUME /var/lib/mysql
ADD cmd.sh /cmd.sh
RUN chmod +x /cmd.sh

ENTRYPOINT /cmd.sh
#CMD usr/sbin/mysqld

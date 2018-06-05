set -e

USER=${USER:=""}
PASS=${PASS:=""}

#contra=$(python /usuario.py $ENV)
#
#if [ ! -d /var/www/html/$ENV ] ;then
#	mkdir /var/www/html/$ENV 
#fi

#useradd dani -p "$contra"  -d /var/www/html/$ENV -s /bin/bash
#chown $ENV:$ENV /var/www/html/$ENV
#service proftpd start
python /usuario.py $USER $PASS
exec proftpd --nodaemon

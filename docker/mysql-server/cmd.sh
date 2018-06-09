set -e

chown -R mysql:mysql /var/lib/mysql
mysql_install_db --user mysql > /dev/null

MYSQL_DATABASE=${MYSQL_DATABASE:-""}
MYSQL_USER=${MYSQL_USER:-""}
MYSQL_PASSWORD=${MYSQL_PASSWORD:-""}

tfile=`mktemp`
cat << EOF > $tfile
USE mysql;
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
UPDATE user SET password=PASSWORD('root') WHERE user='root';
EOF

#if [[ $MYSQL_USER != "" ]]; then
echo "CREATE DATABASE IF NOT EXISTS \`$MYSQL_DATABASE\`;" >> $tfile
echo "GRANT ALL ON \`$MYSQL_DATABASE\`.* to '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';" >> $tfile
#fi

/usr/sbin/mysqld --bootstrap --verbose=0 < $tfile
rm -f $tfile

exec /usr/sbin/mysqld

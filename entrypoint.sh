#!/bin/bash
# Please do not set -e. This may cause all hell to break loose
#set -e

# Django app shutting down.
function shut_down() {
	echo "Dashboard application shutting down..."
	exit
}
trap "shut_down" SIGKILL SIGTERM SIGHUP SIGINT EXIT

# Check if MYSQL parameters are defined in the env. If not, assume SQLite
env | grep MYSQL > /dev/null
if [ $? -eq 0 ]; then

	# Assuming MYSQL parameters are defined correctly
	mysql_settings_file="/usr/src/app/test_pro/settings.py.mysql"

	dbname=`env | grep MYSQL_DATABASE | cut -d"=" -f2`
	passwd=`env | grep MYSQL_ROOT_PASSWORD | cut -d"=" -f2`
	port=`env | grep TCP_PORT | cut -d"=" -f2`
	address=`env | grep TCP_ADDR | cut -d"=" -f2`

	sed -i "s/MYDBNAME/$dbname/g"	$mysql_settings_file
	sed -i "s/MYPASSWORD/$passwd/g"	$mysql_settings_file
	sed -i "s/MYDB_IP/$address/g"	$mysql_settings_file
	sed -i "s/MYDB_PORT/$port/g"	$mysql_settings_file

	# Replace settings.py file
	mv $mysql_settings_file /usr/src/app/test_pro/settings.py

elif [ ! -f /usr/src/app/db/db.sqlite3 ]; then

	# Assuming SQLite. If db.sqlite3 files exits, use that as DB.
	# Else use schema SQL to generate a empty DB.
	echo "Creating Dashboard database"
	sqlite3 /usr/src/app/db/db.sqlite3 < /usr/src/app/DBschema/dashboard_lite_schema.sql

fi

exec "$@"

#!/bin/bash

# Before running this script, ensure you have the settings.py.mysql and
# dashboard_my_schema.sql files copied into this directory (where this script is).
# Then create two directories, litedb and mydb.
# Copy the db.sqlite3 file into litedb/

cwd=$PWD

# Run mysql container
id=`docker run -v $cwd/dashboard_my_schema.sql:/docker-entrypoint-initdb.d/dashboard_my_schema.sql -v $cwd/mydb/:/var/lib/mysql -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=dbpassword -d mysql:latest`

# Let mysql come up
sleep 30

address=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' $id`
port=`docker inspect --format='{{range $p, $conf := .Config.ExposedPorts}} {{$p}} {{end}}' $id | cut -d'/' -f1`

mysql_settings_file="$cwd/settings.py.mysql"

sed -i "s/MYDBNAME/mydashboard/g"  $mysql_settings_file
sed -i "s/MYPASSWORD/dbpassword/g" $mysql_settings_file
sed -i "s/MYDB_IP/$address/g"      $mysql_settings_file
sed -i "s/MYDB_PORT/$port/g"       $mysql_settings_file

# Run django app with db.sqlite3 mounted from host.
# Then inside the container run -
# 	python manage.py dumpdata > db/datadump.json
# 	cp test_pro/settings.py.mysql test_pro/settings.py
# 	python manage.py loaddata db/datadump.json

docker run -v $mysql_settings_file:/usr/src/app/test_pro/settings.py.mysql -v /root/test/litedb/:/usr/src/app/db/ -P -it my-django-app bash -c "python manage.py dumpdata > db/datadump.json && cp test_pro/settings.py.mysql test_pro/settings.py && python manage.py loaddata db/datadump.json"


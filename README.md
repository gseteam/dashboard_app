GSE Dashboard

GSE Dashboard is a people-to-task tracking tool written in Django. It has been written to work with:
  - Embedded database - SQLite3
  - MySQL

You can track:
  - Active/Inactive tasks
  - People associated with the task
  - People over or under-utilized

### Version
1.0

### Build
The first thing you have to do once you download the repository is to build the Docker container for the application. From the root directory of the repository run:
```sh
$ docker build -t my-django-app .
```

### Start App with SQLite DB
Start the my-django-app server with empty SQLite3 database. Here the SQLite DB exists only for the duration that the container is alive.
```sh
$ docker run -P -d my-django-app
```

Start the my-django-app server with empty SQLite3 database. This time, mount a host directory to the container DB directory.
The SQLite DB file created (and modified) will remain even after the container is killed/removed.
```sh
$ docker run -v <some host directory>:/usr/src/app/db/ -P -d my-django-app
```

Start the my-django-app server with a pre-existing SQLite3 database. This time, mount the db.sqlite3 SQLite3 file from the host.
```sh
$ docker run -v <some host directory>/db.sqlite3:/usr/src/app/db/db.sqlite3 -P -d my-django-app
```

### Start App with MySQL DB
You can start the mysql container with no existing mySQL DB. But you need to provide a insput schema file. To use GSE Dashboard app, attach the schema SQL file that is available in Git.
Then, start the my-django-app server and provide the following environment variables:
  - MYSQL_DATABASE - DB name
  - MYSQL_ROOT_PASSWORD
  - TCP_ADDR - this can be host or container IP. If you are using bridge networking and give the container IP/PORT, note that both containers need to run on the same host. If you are using host IP/PORT, it doesn't matter if you are using bridge or overlay networking.
  - TCP_PORT - The corresponding host/container port.
```sh
$ docker run -v <Schema file location>:/docker-entrypoint-initdb.d/dashboard_my_schema.sql -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=<password> -d -P mysql:latest
$ docker run -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=<password> -e TCP_ADDR=<host or container IP> -e TCP_PORT=<host or container port> -P -d my-django-app
```
In the above approach, the mysql DB exists only for the duration that the container is alive.

You can also start the mysql container with no existing DB, but map a host directory into the container  so that the DB lives even after the mysql container is stopped/killed.
```sh
$ docker run -v <Schema file location>:/docker-entrypoint-initdb.d/dashboard_my_schema.sql -v /my/data/directory:/var/lib/mysql -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=<password> -d -P mysql:latest
$ docker run -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=<password> -e TCP_ADDR=<host or container IP> -e TCP_PORT=<host or container port> -P -d my-django-app
```
You can also start the mysql container with an already existing DB. Since we are again mapping a host directory into the container, the updated data will live even after the mysql container is stopped/killed.
```sh
$ docker run -v /my/data/directory:/var/lib/mysql -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=<password> -d -P mysql:latest
$ docker run -e MYSQL_DATABASE=mydashboard -e MYSQL_ROOT_PASSWORD=<password> -e TCP_ADDR=<host or container IP> -e TCP_PORT=<host or container port> -P -d my-django-app
```

### Accessing the application
For each case above, once the container starts running, check the host port that is mapped to the container's 8000 port.
Then use "http://host-ip:host-mapped-port/home" URL to access the tool.

### Todos

 - Make it work with a NOSQL DB
 - Fix threshold errors



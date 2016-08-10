E Dashboard

GSE Dashboard is a people-to-task tracking tool written in Django. It has been written to work with:
  - Embedded database - SQLite3
  - MySQL (TBD)

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

### Build
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
For each case above, check the host port that is mapped to the container's 8000 port.
Then use "http://<host ip or hostname>:<host mapped port>/home" URL to access the tool.

### Todos

 - Make it work with MySQL
 - Make it work with a NOSQL DB
 - Fix threshold errors
 - 



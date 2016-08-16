FROM django:1.9.8

# There are some issues in our code with 1.10.
# Need to fix that.
#FROM django:latest

COPY app1 /usr/src/app/app1/
COPY manage.py  /usr/src/app/
COPY test_pro /usr/src/app/test_pro/

# Folder where db files are created when using SQLite.
# We need to mount this to a host dir to keep it persistent.
RUN mkdir /usr/src/app/db/

# Keep the SQLite schema in the app container - in case I
# want a embedded DB (and I dont have a db.sqlite3 DB file yet.
COPY db/dashboard_lite_schema.sql /usr/src/app/DBschema/

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /usr/src/app

EXPOSE 8000
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


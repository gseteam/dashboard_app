FROM django:latest

COPY app1  /usr/src/app/app1/
COPY manage.py  /usr/src/app/
COPY test_pro /usr/src/app/test_pro/

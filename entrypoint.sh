#!/bin/bash
set -e

# Django app shutting down.
function shut_down() {
  echo "Dashboard application shutting down..."
  exit
}

trap "shut_down" SIGKILL SIGTERM SIGHUP SIGINT EXIT

if [ ! -f /usr/src/app/db/db.sqlite3 ]; then
  echo "Creating Dashboard database"
  sqlite3 /usr/src/app/db/db.sqlite3 < /usr/src/app/DBschema/dashboard_lite_schema.sql
fi

exec "$@"

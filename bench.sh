#!/usr/bin/env bash

set -e

export DATABASE="$1"
export RUNNING_COCKROACH_BACKEND_TESTS=1

case $DATABASE in
   postgres|cockroach) ;;
   *)
     echo "usage $0 [postgres|cockroach]" && exit 1 ;;
esac

echo "Running benchmarks against $DATABASE..."

docker-compose down
docker-compose up -d $DATABASE
sleep 2
./manage.py flush --noinput
./manage.py migrate
./manage.py populate
pytest -v

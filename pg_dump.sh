#!/bin/bash
set -e

[ -f .env ] && source .env

if [ -z "$DB_USER" ]; then
    echo "ERROR: DB_USER is not defined"
    exit 1
fi
if [ -z "$DB_NAME" ]; then
    echo "ERROR: DB_NAME is not defined"
    exit 1
fi
if [ -z "$1" ]; then
    OUTPUT="db_`date +%FT%T`.dump"
else
    OUTPUT="$1"
fi

pg_dump -Fc -U "$DB_USER" -h localhost "$DB_NAME" \
    | sed "s/$DB_USER/{{DB_USER}}/g" "$OUTPUT" > "$OUTPUT"

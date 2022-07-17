#!/usr/bin/env bash

set -e

pip install psycopg2-binary && pip install --no-cache-dir -r requirements.txt

cd api && flask db upgrade

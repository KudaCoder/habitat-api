#!/usr/bin/env bash

cd api && flask db upgrade &
python wsgi.py

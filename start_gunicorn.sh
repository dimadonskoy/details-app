#!/usr/bin/env bash

####### Start gunicorn #######

##############################

gunicorn -b '0.0.0.0' -w 4 --log-level debug src.details.app:app > gunicorn.log 2>&1 &


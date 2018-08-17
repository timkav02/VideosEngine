#!/bin/bash

NAME="xrdb_app"                                      # Name of the application
DJANGODIR=/var/www/search02/videos                   # Django project directory
SOCKFILE=/var/www/search02/run/gunicorn.sock  	    # we will communicte using this unix socket
USER=Timo                                           # the user to run as
GROUP=Timo                                          # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=videos.settings          # which settings file should Django use
DJANGO_WSGI_MODULE=videos.wsgi                  # WSGI module name
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /var/www/search02/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-

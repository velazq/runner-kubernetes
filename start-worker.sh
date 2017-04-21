#!/bin/sh

celery worker -A runner --prefetch-multiplier 1 -c 1 -q \
  --without-gossip --without-mingle --without-heartbeat \
  # --loglevel=info

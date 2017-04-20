#!/bin/sh

celery worker -A runner --prefetch-multiplier 1 -c 1 \
  --without-gossip --without-mingle --without-heartbeat \
  --loglevel=info \
  # -q

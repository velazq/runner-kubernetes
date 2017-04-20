#!/bin/sh

echo Stopping Redis container...
docker stop redis
echo

echo Stopping RabbitMQ container...
docker stop rabbitmq
echo

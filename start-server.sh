#!/bin/sh

echo Starting RabbitMQ container...
docker run -d -p 5672:5672 --rm --name rabbitmq rabbitmq
echo

echo Starting Redis container...
docker run -d -p 6379:6379 --rm --name redis redis
echo

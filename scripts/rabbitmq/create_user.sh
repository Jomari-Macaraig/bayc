#!/bin/bash

rabbitmqctl add_user ${RABBITMQ_DEFAULT_USER} ${RABBITMQ_DEFAULT_PASS}
rabbitmqctl add_vhost ${RABBITMQ_DEFAULT_VHOST}
rabbitmqctl set_user_tags ${RABBITMQ_DEFAULT_USER} mytag
rabbitmqctl set_permissions -p ${RABBITMQ_DEFAULT_VHOST} ${RABBITMQ_DEFAULT_USER} ".*" ".*" ".*"
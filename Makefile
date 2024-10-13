SHELL := /bin/bash

.PHONY:
	clean
	initialize_database
	initialize_rabbitmq
	start_dev
	build_base
	init_env

help:
	@echo "clean - remove all artifacts"

clean:
	find . -iname "*.pyo" | xargs rm -Rf
	find . -iname "*.pyd" | xargs rm -Rf
	find . -iname "__pycache__" | xargs rm -Rf
	find . -iname "*.pyc" | xargs rm -Rf


initialize_database:
	make clean
	docker compose -f compose/development.yml run -d --rm --name postgres --service-ports postgres
	sleep 10
	. scripts/database/create_user_and_db.sh
	docker stop postgres

initialize_rabbitmq:
	make clean
	docker compose -f compose/development.yml run -d --rm --name rabbitmq --service-ports rabbitmq
	chmod 777 scripts/rabbitmq/create_user.sh
	sleep 10
	docker exec -it rabbitmq  /tmp/scripts/create_user.sh
	docker stop rabbitmq

start_dev:
	make clean
	docker compose -f compose/development.yml run -d --rm --name postgres --service-ports postgres
	docker compose -f compose/development.yml run -d --rm --name rabbitmq --service-ports rabbitmq

build_base:
	make clean
	pip3 install -r requirements/development.txt

initialize_env:
	make build_base
	source scripts/app/create_user.sh
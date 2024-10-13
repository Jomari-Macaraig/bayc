# BAYC NFT Transfer Monitor
A simple django project that monitor BAYC NFT Transfer event

## Requirements
Latest Docker Desktop
- [docker-desktop](https://docs.docker.com/desktop/)

or

Latest Docker and Docker Compose for your OS
- [docker-machine](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)

Postgresql for psql command (optional if will use postgres as database)
- [postgresql](https://www.postgresql.org/download/)


## Setting up development
### 1. Cloning the project.
```commandline
$ git clone <repo-url> bayc
$ cd bayc
```
### 2. Create .env file
Copy the .env.template and update the values and execute it.
### 3. Initialize database and rabbitmq.
This will create user. Please omit this if done previously  
Please see env.template for environment variables to be configured for the project.  
Replace some environment variables for the meantime(we're using __0.0.0.0__ for local setup)
```commandline
$ export POSTGRES_HOST=0.0.0.0
$ export RABBITMQ_HOST=0.0.0.0
```
Run command
```commandline
$ make initialize_database
$ make initialize_rabbitmq
```

Note: Please ignore the part for postgres if you're gonna use sqlite

### 4. Spin up  the services (web, postgres, rabbitmq, celery and celery-beat).
Revert first the environment variables
```commandline
$ export POSTGRES_HOST=postgres
$ export RABBITMQ_HOST=rabbitmq
$ docker compose -f compose/development.yml run -d --rm --name bayc-dev --service-ports web
```
The service should be running properly now
### 5. SSH to the web service
```commandline
$ ssh bayc_super@0.0.0.0 -p 2326
$ sudo su
$ cd /srv/bayc
$ source .env
```
Note:
- Password is *pass@1234* 


### 6. Run migration
```commandline
$ python manage.py migrate
```

### 7. Create Superuser
```commandline
$ python manage.py createsuperuser
```

### 8. Run development server
```commandline
$ python manage.py runserver 0.0.0.0:8000
```

## Management Commands
1. *__bayc_listen_events.py__* - command that listen to Transfer event emitted by the BAYC smart contract.
2. *__bayc_process_past_events.py__* - command to fetch Transfer event emitted by the BAYC smart contract from a block range

### API
1. *__api/v1/bayc/__* - list all Transfer events
2. *__api/v1/bayc/<int: token_id>__* - list all related Transfer events to the token_id provided.


### NOTE:
You can uncomment the postgres configuration in the config.settings.development to use postgres as database
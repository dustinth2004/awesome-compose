## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/django)

### Django application in dev mode

This is a basic Django application that demonstrates how to set up a containerized Django development environment. The project is based on the default `django-admin startproject` template.

Project structure:
```
.
├── compose.yaml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── manage.py
```

*   `compose.yaml`: The Docker Compose file that defines the services, networks, and volumes for the application.
*   `app/Dockerfile`: The Dockerfile for the Django application. It installs the dependencies and runs the development server.
*   `app/requirements.txt`: The Python dependencies for the Django application.
*   `app/manage.py`: The Django command-line utility for administrative tasks.
*   `app/example/`: The directory containing the Django project's settings, URLs, and other configurations.

[_compose.yaml_](compose.yaml)
```
services: 
  web: 
    build: app 
    ports: 
      - '8000:8000'
```

## Deploy with docker compose

```
$ docker compose up -d
Creating network "django_default" with the default driver
Building web
Step 1/6 : FROM python:3.7-alpine
...
...
Status: Downloaded newer image for python:3.7-alpine
Creating django_web_1 ... done

```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
3adaea94142d        django_web          "python3 manage.py r…"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp   django_web_1
```

After the application starts, navigate to `http://localhost:8000` in your web browser:

Stop and remove the containers
```
$ docker compose down
```

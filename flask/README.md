## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/flask)

### Python/Flask application

This is a simple "Hello World" application using the Flask framework. The purpose of this sample is to demonstrate how to create a containerized Flask application using Docker Compose.

Project structure:
```
.
├── compose.yaml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

*   `compose.yaml`: The Docker Compose file that defines the services, networks, and volumes for the application.
*   `app/Dockerfile`: The Dockerfile for the Flask application. It installs the dependencies and runs the application.
*   `app/requirements.txt`: The Python dependencies for the Flask application.
*   `app/app.py`: The main Flask application file. It contains a single route that returns "Hello World!".

[_compose.yaml_](compose.yaml)
```
services: 
  web: 
    build:
     context: app
     target: builder
    ports: 
      - '8000:8000'
```

## Deploy with docker compose

```
$ docker compose up -d
[+] Building 1.1s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                       0.0s
    ...                                                                                                                                         0.0s
 => => naming to docker.io/library/flask_web                                                                                                                                                                                               0.0s
[+] Running 2/2
 ⠿ Network flask_default  Created                                                                                                                                                                                                          0.0s
 ⠿ Container flask-web-1  Started
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
flask-web-1         "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp
```

After the application starts, navigate to `http://localhost:8000` in your web browser or run:
```
$ curl localhost:8000
Hello World!
```

Stop and remove the containers
```
$ docker compose down
```

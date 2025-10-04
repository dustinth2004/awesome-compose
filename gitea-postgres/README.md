## Gitea with PostgreSQL

This example demonstrates how to set up Gitea with a PostgreSQL database using Docker Compose. Gitea is a lightweight and self-hosted Git service.

Project structure:
```
.
├── compose.yaml
└── README.md
```

*   `compose.yaml`: The Docker Compose file that defines the `gitea` and `db` services.

[_compose.yaml_](compose.yaml)
```
services:
  gitea:
    image: gitea/gitea:latest
    ports:
      - 3000:3000
    ...
  db:
    image: postgres:alpine
    environment:
    ...
```

When deploying this setup, docker compose maps the gitea container port 3000 to
the same port of the host as specified in the compose file.

## Deploy with docker compose

```
$ docker compose up -d
Creating network "gitea-postgres_default" with the default driver
Creating gitea-postgres_db_1 ... done
Creating gitea-postgres_gitea_1 ... done
Attaching to gitea-postgres_db_1, gitea-postgres_gitea_1
....
Starting gitea-postgres_db_1 ... done
Starting gitea-postgres_gitea_1 ... done
```


## Expected result

Check containers are running and the port mapping:
```
$ docker ps
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                          NAMES
2f5624043da9        gitea/gitea:latest   "/usr/bin/entrypoint…"   56 seconds ago      Up 16 seconds       22/tcp, 0.0.0.0:3000->3000/tcp gitea-postgres_gitea_1
86acc768453e        postgres:alpine      "docker-entrypoint.s…"   57 seconds ago      Up 17 seconds       5432/tcp                       gitea-postgres_db_1
```

Navigate to `http://localhost:3000` in your web browser to access the installed
Gitea service.

![page](output.jpg)

Stop and remove the containers

```
$ docker compose down
```

To remove all Gitea data, delete the named volumes by passing the `-v` parameter:
```
$ docker compose down -v
```

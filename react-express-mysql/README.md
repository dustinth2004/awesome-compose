## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/react-express-mysql)

### React application with a NodeJS backend and a MySQL database

This example demonstrates a full-stack application with a React frontend, an Express (Node.js) backend, and a MySQL database.

### Project Structure

```
.
├── backend
│   ├── Dockerfile
│   ├── src
│   │   ├── index.js
│   │   └── ...
│   └── ...
├── db
│   └── password.txt
├── compose.yaml
├── frontend
│   ├── Dockerfile
│   ├── src
│   │   └── App.js
│   └── ...
└── README.md
```

*   `compose.yaml`: The Docker Compose file that defines the `frontend`, `backend`, and `db` services.
*   `backend/`: Contains the source code for the Express backend.
*   `frontend/`: Contains the source code for the React frontend.
*   `db/`: Contains the password file for the database.

### Services

*   **frontend**: The React application.
*   **backend**: The Express backend, which provides the API for the frontend.
*   **db**: The MySQL database.

> ℹ️ **_INFO_**  
> For compatibility purpose between `AMD64` and `ARM64` architecture, we use a MariaDB as database instead of MySQL.  
> You still can use the MySQL image by uncommenting the following line in the Compose file   
> `#image: mysql:8.0.27`

## Deploy with docker compose

```
$ docker compose up -d
```

## Expected result

After the application starts, navigate to `http://localhost:3000` in your web browser.

![page](./output.png)


The backend service container has the port 80 mapped to 80 on the host.
```
$ curl localhost:80
{"message":"Hello from MySQL 8.0.19"}
```

Stop and remove the containers
```
$ docker compose down
```

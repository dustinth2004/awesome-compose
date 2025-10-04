## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/react-express-mongodb)

### React application with a NodeJS backend and a MongoDB database

This example demonstrates a full-stack application with a React frontend, an Express (Node.js) backend, and a MongoDB database.

### Project Structure

```
.
├── backend
│   ├── Dockerfile
│   ├── server.js
│   └── ...
├── compose.yaml
├── frontend
│   ├── Dockerfile
│   ├── src
│   │   └── App.js
│   └── ...
└── README.md
```

*   `compose.yaml`: The Docker Compose file that defines the `frontend`, `server` (backend), and `mongo` services.
*   `backend/`: Contains the source code for the Express backend.
*   `frontend/`: Contains the source code for the React frontend.

### Services

*   **frontend**: The React application, served by a Node.js server.
*   **server**: The Express backend, which provides the API for the frontend.
*   **mongo**: The MongoDB database.

## Deploy with docker compose

```
$ docker compose up -d
```

## Expected result

After the application starts, navigate to `http://localhost:3000` in your web browser.

![page](./output.png)

Stop and remove the containers
```
$ docker compose down
```

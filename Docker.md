# Docker
An engine that runs containers.

1. Solves dependency conflicts
Each app runs inside its own container with its own dependencies.
Each container encapsulates its own dependencies.

2. Allows easy scaling up
When a server application needs to handle a higher usage than what a single server can handle, the solution is: placing a reverse proxy in front of it, and duplicate the server as many times as needed.

3. Allows seamless upgrades

## Basic Concepts


- Container: contains everything an app needs to run
- Images: any container that runs is created from an *image*.
    - describe everything that's needed to create a container; it is a template for containers
- Registries: where images are stored

## Use Docker Image

### Container Management Commands
- `docker ps` lists the containers that are still running. Add the `-a` switch in order to see containers that have stopped

- `docker logs` retrieves the logs of a container, even when it has stopped

- `docker inspect` gets detailed information about a running or stopped container

- `docker stop` stops a container that is still running

- `docker rm` deletes a container

- `docker container prune -f` deletes all stopped containers

### Running a Server Container

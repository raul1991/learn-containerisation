# Commands used in this session

### Building a Docker image

> docker build -t `<some-name>` `<path-to-the-build-context>`

**Example**: 

> docker build -t foo . (here the build context is my current directory)

> docker build -t foo a-dir (here the build context is the 'a-dir' directory)

### Running a container with the built image

> docker run `<some-name>`

### Going inside a running container

> docker exec -it `<container-id>` bash

### Port forwarding in docker

> docker run -p `<host-port>`:`<container-port>` `<some-name>`

**Example**: 

> docker run -p 9000:9000 foo

### Seeing which containers are currently running

> docker container ps

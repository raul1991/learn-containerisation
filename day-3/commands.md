# docker build command - builds the Docker image

`docker build -t <some-name> <path-to-the-build-context>`

Example: docker build -t foo . (here the build context is my current directory)

# docker run command - runs the built image

`docker run <some-name>`

# going inside a running container

`docker exec -it <container-id> bash`

# port forwarding in docker

`docker run -p <host-port>:<container-port> <some-name>`
Example: docker run -p 9000:9000 foo

# seeing which containers are currently running
`docker container ps`

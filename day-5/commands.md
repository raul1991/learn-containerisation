# Commands learnt

- Pulling an image from a registry

```

docker pull <registry>/<repo-name>/<image-name>:<tag> (uses docker.io as registry by default)

```

Example:

```

docker pull cafebabe1991/coba-learning:v1

```

- Running an image from a repo directly

Example:

```

docker run -p 9000:9000 cafebabe1991/coba-learning:v1

```

- Running with interactive terminal so docker container can be killed

```

docker run -it <some-image>

```

Example:

```

docker run -it -p 9000:9000 cafebabe1991/coba-learning:v1

```

- Overriding env variables created in docker file

```
Say, I have the following content in my Dockerfile

FROM python:slim

... some more docker stuff

ENV PORT_HTTP 5555
```


To override PORT_HTTP, provide values for it in the run command

Example:

```
docker run -it -ePORT_HTTP=9090 <some-image>

```

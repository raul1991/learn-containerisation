# Commands learnt

- Attaching a 'host only volume'

```
docker run -v /tmp/:/tmp/ <some-image>
```

Example:

```
docker run -v /tmp/:/tmp/ -p 9000:9000 cafebabe1991/coba-learning:v1
```

- Attaching a volume in read only mode

```
docker run -v /tmp/:/tmp/:ro -p 9000:9000 cafebabe1991/coba-learning:v1
```

- Attaching an 'anonymous volume'

```
docker run -v /tmp/ <some-image>
```

Example:

```
docker run -p 9000:9000 -v /tmp/ cafebabe1991/coba-learning:v1
```

- Attaching a 'named volume'

1. Create a volume

``` 
docker volume create my-named-volume 
```

2. Attach it to your docker container

``` 
docker run -v my-named-volume:/tmp/ -p 9000:9000 cafebabe1991/coba-learning:v1 
```

- Inspect a docker container

``` 
docker inspect <container id>
```

- Inspect a volume

``` 
docker inspect <volume-name-or-its-hash> 
```

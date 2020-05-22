# Question asked

What if I don't expose a port and still forward it from outside ?

- It means you are trying to forward network packets to a port that is not serving anything. Expose is a way to let a port inside your docker be exposed for traffic from your host machine, provided port forwarding is done properly.

What is the difference between Entrypoint and CMD ?

- Entrypoint serves as a default command while cmd is additional arguments to it. Cmd can be overridden from the docker run command like

``` 

docker run <image> command

```

In the above command, "command" is what replaces the cmd inside the docker.

What happens if I give multiple cmds ?

- Only the last one will be executed.

Can I execute multiple commands ?

- Yeah. Just make a script and call that from CMD

# Video

[![Watch the video](/day-2/lecture-2-github.png)](https://youtu.be/X4DQbey0Iys)
# Agenda

- What is the difference between a Dockerfile and docker container ?
- What are basic parts of a docker file. Not all, just some parts are discussed.
  - base type (OS)
  - some modifications (libraries)
  - some ports to be exposed (configuration)
  - A final command to be run (init script)

- Create a simple Dockerfile and categorise them into
the steps above.
- Understand and annotate the contents of it.

# Exercise

- Try copying a file into the docker using the COPY
command in the dockerfile.

Syntax: 

COPY `<host path>` `<docker path>`

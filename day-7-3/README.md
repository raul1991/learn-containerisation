#Video

[![Watch the video](/day-7-3/lecture-7-3-github.png)](https://youtu.be/0O1NRNdihyk)

# Agenda

- We are dockerizing the rest backend in this application.
- Watch the above video.

# Build instructions

- Run the following in the hashtag-monitor folder to build docker image

```
 docker build -t hashtag-monitor .
```

- Run the container with that image

```
 docker run -p 5000:5000 -ti hashtag-monitor
```

- Go to https://localhost:5000/search/tag on your browser

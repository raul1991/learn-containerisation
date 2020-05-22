# base type (os)
FROM python:slim

# COPY FILE INTO DOCKER
COPY ./run.sh /

# modifications
RUN chmod +x /run.sh && apt-get update && apt-get install -y curl

# configuration
ENV PYTHONUNBUFFERED=1
ENV PORT_HTTP 9000
EXPOSE $PORT_HTTP

# init script
ENTRYPOINT ["python", "-c"]

# default command
CMD ["/run.sh"]

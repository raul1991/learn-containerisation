# base type (os)
FROM python:slim

# COPY FILE INTO DOCKER
COPY ./run.sh /

# modifications
RUN chmod +x /run.sh && apt-get update && apt-get install -y curl

# configuration
ENV PYTHONUNBUFFERED=1
EXPOSE 9000 9001

# init script
CMD ["/run.sh"]

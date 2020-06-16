# base type (os)
ARG BASE_IMAGE

FROM $BASE_IMAGE

# COPY FILE INTO DOCKER
COPY ./init.sh /

# modifications
RUN chmod +x /init.sh && apt-get update && apt-get install -y curl

# configuration
ENV PYTHONUNBUFFERED=1
ENV HTTP_PORT_1 9000
ENV HTTP_PORT_2 9001

EXPOSE $HTTP_PORT_1 $HTTP_PORT_2

# init script
CMD ["/init.sh"]

# base type (os)
FROM python:slim

# modifications
RUN apt-get update && apt-get install -y curl

COPY ./foo.txt /

COPY ./init.sh /

RUN chmod +x /init.sh

# configuration
ENV PYTHONUNBUFFERED=1
EXPOSE 9001 9002

# init script
CMD ["/init.sh"]

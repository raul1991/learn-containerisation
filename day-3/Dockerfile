# base type (os)
FROM python:slim

# modifications
RUN apt-get update && apt-get install -y curl

COPY ./foo.txt /

# configuration
ENV PYTHONUNBUFFERED=1
EXPOSE 9001

# init script
CMD ["python", "-m", "http.server", "9001"]

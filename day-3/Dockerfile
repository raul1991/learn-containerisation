# base type (os)
FROM python:slim

# modifications
RUN apt-get update && apt-get install -y curl

# configuration
ENV PYTHONUNBUFFERED=1
EXPOSE 9000

# init script
CMD ["python", "-m", "http.server", "9000"]

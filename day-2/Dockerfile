# Base type

# its an os (linux flavour with python installed on it.)
# slim - refers to a tag which is lightweight linux with python installed on it.
FROM python:slim

# Install Libraries (-y is required to force install)
RUN apt-get update && apt-get install -y vim

# Ports or configurations
EXPOSE 9000
ENV PYTHONUNBUFFERED=1
# Run or init step
CMD ["python", "-m", "http.server", "9000"]

# Base type
FROM python:slim

# modifications
ENV REST_PORT 5000
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /

# ports
EXPOSE $ENV_PORT

# init script
CMD ["python", "app.py"]
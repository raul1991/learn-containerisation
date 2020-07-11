# Base type
FROM python:3

# modifications
ENV REST_PORT 5000
COPY requirements.txt /
RUN pip install -r /requirements.txt && apt-get install -y default-libmysqlclient-dev
COPY . /

# ports
EXPOSE $ENV_PORT

# init script
CMD ["python", "app.py"]
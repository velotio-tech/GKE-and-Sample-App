FROM ubuntu:16.04
COPY src/requirements.txt .
RUN apt-get update
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python python-dev python-distribute python-pip libmysqlclient-dev
RUN pip install -r requirements.txt
RUN apt-get install -y mysql-client
RUN mkdir /code
COPY src /code
WORKDIR /code
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
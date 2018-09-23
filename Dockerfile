FROM python:3.6.6-slim-stretch
COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DOTENV_PATH /app/.env

RUN find /app -name '*.pyc' -delete
RUN find /app -name '__pycache__' -delete
RUN find /app -name '000*.py' -delete
RUN rm -fr .idea .git* .python-version package-lock.json .pytest_cache
RUN find . -name '*.pyc' -delete
RUN find . -name '__pycache__' -delete


RUN apt update && apt install -y git $(cat apt-get-dependencies.txt)

RUN apt clean
RUN apt autoclean

RUN pip install -r requirements-dev.txt
RUN touch .env

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install nodejs --assume-yes
RUN npm -v
RUN npm install -g bower

FROM python:3.6.6-slim-stretch
LABEL maintainer controlapet-prod
COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV DOTENV_PATH /app/.env

RUN find /app -name '*.pyc' -delete
RUN find /app -name '__pycache__' -delete
RUN rm -fr .idea .git* .python-version package-lock.json .pytest_cache


RUN apt update && apt install -y git $(cat apt-get-dependencies.txt)

RUN apt clean
RUN apt autoclean

RUN pip install -r requirements-dev.txt
RUN touch .env

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD python manage.py runserver 0.0.0.0:$PORT

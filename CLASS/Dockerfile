# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR python-docker

EXPOSE 5000

COPY . .

ENV FLASK_APP='cars.py'

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# learningmw1991/restapi_cars
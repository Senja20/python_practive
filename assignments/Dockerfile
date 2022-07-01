FROM python:3.9-alpine

WORKDIR /tmp

RUN apk update && apk add build-base

RUN pip install --upgrade pip && \
    pip install \
    faker \
    flask \
    flask-restful \
    jsonschema \
    pexpect \
    pytest \
    pytest-repeat \
    pytest-xdist \
    requests \
    sqlalchemy

WORKDIR /app

COPY *.py *.sql ./
COPY solutions solutions

ARG ASSIGNMENT=1
ENV ASSIGNMENT=$ASSIGNMENT

ENTRYPOINT ["py.test", "--verbose", "--color=yes", "--tb=short"]

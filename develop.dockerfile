FROM python:3.8.2-alpine

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev make postgresql-dev

RUN pip install pipenv

# create root directory
RUN mkdir /app/

# install dependicies
COPY Pipfile app/Pipfile
COPY Pipfile.lock app/Pipfile.lock
RUN cd /app && pipenv install --dev --system --deploy --ignore-pipfile

# copy all file to their specific directory
COPY src/ /app/src/
COPY tests/ /app/tests/

COPY setup/scripts/ app/scripts

WORKDIR /app/src/

ENV PYTHONPATH=/app/
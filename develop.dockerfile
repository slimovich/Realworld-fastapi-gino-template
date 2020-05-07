FROM python:3.8.2-alpine

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev make libxslt-dev libxml2-dev

RUN pip install pipenv

# create root directory
RUN mkdir /app/

# install dependicies
COPY Pipfile app/Pipfile
COPY Pipfile.lock app/Pipfile.lock
RUN cd /app && pipenv install --dev --system --deploy --ignore-pipfile

# copy all file to their specific directory
COPY . /app/

WORKDIR /app/src/

ENV PYTHONPATH=/app/
FROM python:3.8.2-alpine

RUN pip install pipenv

# create root directory
RUN mkdir /app/

# install dependicies
COPY Pipfile app/Pipfile
COPY Pipfile.lock app/Pipfile.lock
RUN cd /app && pipenv install --system --deploy --ignore-pipfile

# copy all file to their specific directory
COPY src/ /app/src/

COPY setup/scripts/start.sh app/

WORKDIR /app/src/

ENV PYTHONPATH=/app/
# Python 3.10 Alpine Base Image
FROM python:3.10-alpine

# Set Working Directory
WORKDIR /app

# Upgrade Pip
RUN pip install --upgrade pip

# Install Postgres Dependencies
RUN apk add --no-cache postgresql-libs postgresql-dev gcc musl-dev libffi-dev

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Install Dependencies
ADD pyproject.toml poetry.lock /app/
RUN poetry install --without dev --no-ansi

# Add Application
ADD . /app/

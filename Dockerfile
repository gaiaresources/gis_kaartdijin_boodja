# Node 18 Alpine Base Image
FROM node:18-alpine as frontend

# Set Working Directory
WORKDIR /app/

# Install Dependencies
ADD kaartdijin_boodja/frontend/kaartdijin_boodja/package*.json /app/
RUN npm ci

# Add Frontend App
ADD kaartdijin_boodja/frontend/kaartdijin_boodja/ /app/

# Build
RUN npm run build

# Remove Node Modules
RUN rm -rf node_modules

# Python 3.10 Alpine Base Image
FROM python:3.10-alpine as backend

# Set Working Directory
WORKDIR /app/

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

# Add Backend App
ADD . /app/

# Copy Built Frontend
COPY --from=frontend /app/ kaartdijin_boodja/frontend/kaartdijin_boodja/

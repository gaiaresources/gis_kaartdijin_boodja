# Python 3.10 Base Image
FROM python:3.10-slim

# Install Pip
RUN pip install --upgrade pip

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Set Working Directory
WORKDIR /app/

# Install Dependencies
COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install --without dev --no-ansi

# Copy Application
COPY ./ /app/

# (Dev) Set Environment Variables
ENV PORT=8000
ENV HOST=0.0.0.0
ENV DEBUG=true
ENV SECRET_KEY=django-insecure
ENV DATABASE_URL=sqlite://./sqlite.db

# (Dev) Migrate Database, Load Test Fixtures and Run Server
RUN python3 manage.py migrate
RUN python3 manage.py loaddata tests/fixtures/*/*.json
CMD python3 manage.py runserver $HOST:$PORT
EXPOSE $PORT

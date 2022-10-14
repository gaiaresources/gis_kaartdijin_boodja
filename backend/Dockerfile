FROM python:3.10-slim

RUN pip install --upgrade pip

WORKDIR /app/
COPY ./pyproject.toml ./poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./ /app/

ENV PORT=8000
ENV HOST=0.0.0.0
ENV DEBUG=true
ENV SECRET_KEY=django-insecure
ENV DATABASE_URL=sqlite://./sqlite.db

RUN python3 manage.py migrate
RUN python3 manage.py loaddata tests/fixtures/*/*.json
CMD python3 manage.py runserver $HOST:$PORT
EXPOSE $PORT

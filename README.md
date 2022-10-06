# Kaartdijin Boodja
Kaartdijin Boodja (_meaning "Knowledge of Country"_) is a web application for managing a catalogue of GIS layers and
publishing them for the Department of Biodiversity, Conservation and Attractions (DBCA).

## Table of Contents
1. [Backend](#backend)
    1. [Requirements](#requirements)
    2. [Development](#development)
        1. [Installation][#installation]
        2. [Usage][#usage]
    3. [Configuration](#configuration)
    4. [Structure](#structure)
2. [Frontend](#frontend)
    1. [Requirements](#requirements-1)
    2. [Development](#development-1)
        1. [Installation](#installation-1)
        2. [Building](#building)
        2. [Development Environment](#development-environment)
    3. [Configuration](#configuration-1)
    4. [Structure](#structure-1)

## Backend
The backend of Kaartdijin Boodja is a [Python](https://www.python.org/) [Django](https://www.djangoproject.com/) project
using [Django REST Framework](https://www.django-rest-framework.org/) backed by a [PostgreSQL](https://www.postgresql.org/)
database. The backend uses [Poetry](https://python-poetry.org/) to manage its dependencies, and is linted, type-checked
& unit-tested using `flake8`, `mypy` and `pytest`.

### Requirements
* [Python 3.10](https://www.python.org/downloads/release/python-3100/)
* [Poetry](https://python-poetry.org/)

### Development
#### Installation
To get a standard development environment up and running using Poetry and virtual environments:
```shell
# Ensure that Python 3.10 is currently activated
$ python3 --version
Python 3.10.4

# Create a virtual environment and install dependencies using Poetry
# The dependencies are installed from the `poetry.lock` file, providing
# consistent and reproducible installations across any machine.
$ poetry install

# Enter the Poetry virtual environment shell before usage
$ poetry shell
```

#### Usage
Linting, type checking and unit testing are managed using the `poe` task runner:
```shell
$ poe lint
$ poe type
$ poe test
```

To run a development server, use the `Django` `manage.py` script:
```shell
$ DEBUG=True python3 manage.py runserver
```

### Configuration
The backend requires the following environment variables to be set:
```
SECRET_KEY=...
DATABASE_URL=...
```
For convenience, these can also be defined in a `.env` file that will be loaded at runtime.

### Structure
The backend is structured as a traditional Django project using Django REST Framework, with two internal Django
"apps" (the Catalogue and Publisher).

For more information on the project structure, see the following links:
* [DBCA-WA Django Base Template](https://github.com/dbca-wa/django-base-template)
* [WeMake Typed Django Template](https://github.com/wemake-services/wemake-django-template)
* [Django Quickstart](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
* [Django REST Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)

## Frontend
The frontend of Kaartdijin Boodja is a ...

### Requirements
* NodeJS ...
* NPM ...

### Development
#### Installation
Standard fare:
* `npm i` to install and/or appropriately update packages and their dependencies
* `npm ci` to clean install, which installs the exact versions of all packages and dependencies listed in the
  `package-lock.json` file. Using the `ci` flag is deterministic and reproducible.

#### Building
`npm build`, Viola!

#### Development Environment
`npm dev`

### Configuration
The frontend requires the following...

### Structure
The frontend is broadly split into 3 layers.
They are:
- `backend`
  - Concerned with fetching raw data from external sources
  - Does little to no processing or data transformation
- `stores` (conceptually 'providers' combined with storage)
  - Transforms the results from the backend into a form more appropriate for storage.
    e.g. two different actions might get and store different subsets of the same `backend` data
  - Returns a composable with the store itself, publicly exposed getters, and actions for the store.
    - The store contains the fetched data and prompts an update of the component when updated
    - Getters fetch data and update the store
      - Equivalent to `computed()`
    - Actions fetch data from the `backend` and mutate the store.
      - Equivalent to component methods
      - They can be asynchronous, meaning they can be `await`'ed
- `components`
  - The views that import the store composables and call getters and actions

Lower layers should not call or use definitions of higher layers.
e.g. the call chain would be `component` --> `store` action --> `backend`

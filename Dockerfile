FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTCODE=1 \
	PIP_NO_CACHE_DIR=off \
	PIP_DEFAULT_TIMEOUT=100 \
	POETRY_HOME="/opt/poetry" \
	POETRY_VIRTUALENVS_CREATE=0 \
  PYTHONPATH=/app

ENV PATH="$PATH:$POETRY_HOME/bin"

WORKDIR /app/

RUN apt-get update -y && apt install build-essential curl --no-install-recommends -y && curl -sSL https://install.python-poetry.org | python3 -

COPY . /app

RUN poetry config virtualenvs.create false && poetry install --without dev
RUN opentelemetry-bootstrap --action=install

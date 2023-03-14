FROM python:3.10-slim as python
ENV PYTHONUNBUFFERED=true
WORKDIR /usr/src/app


FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN poetry install --no-root --no-interaction --no-ansi -vvv



FROM python as runtime
ENV PATH="/usr/src/app/.venv/bin:$PATH"
COPY --from=poetry /usr/src/app /usr/src/app
EXPOSE 50051
CMD python main.py
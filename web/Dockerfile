FROM python:3.11.2-slim-bullseye

RUN apt-get update && \
    apt-get upgrade --yes

RUN useradd --create-home realpython
USER realpython
WORKDIR /Users/will

ENV VIRTUALENV=/Users/will/page-tracker/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=realpython pyproject.toml constraints.txt ./
RUN echo "Debug: Installed system dependencies" && \
    python -m pip install --upgrade pip setuptools && \
    python -m pip install --no-cache-dir -c constraints.txt ".[dev]"

COPY --chown=realpython src/ src/
COPY --chown=realpython test/ test/

RUN echo "Debug: Installed project dependencies" && \
    python -m pip install . -c constraints.txt && \
    python -m pytest test/unit/ --flask-url http://localhost:8082 --redis-url redis://localhost:6379 && \

    python -m pip wheel --wheel-dir dist/ . -c constraints.txt

# Add logging to a file
RUN echo "Logging: Building the Docker image is complete" > build_log.txt

CMD ["flask", "--app", "page_tracker.app", "run", \
     "--host", "0.0.0.0", "--port", "5000"]

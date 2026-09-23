# Reliable Kafka Platform

An incremental platform-engineering lab for building, observing, and safely
changing a Kafka-compatible service.

The repository evolves through small pull requests. Every change must pass CI
and remain reviewable before it reaches the protected `main` branch.

## Delivery path

```text
AI-authored branch -> pull request -> CI -> human review -> merge
```

Production deployment will be introduced in a later milestone and will retain
a separate human approval gate.

## Milestone 1: minimal operational service

The first pull request introduces only the smallest testable service:

- `GET /health` reports process health.
- `GET /version` identifies the environment, release, and Git commit.
- GitHub Actions checks formatting, lint, and tests on every pull request.

### Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` or request:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/version
```

### Validate

```bash
ruff format --check .
ruff check .
pytest
```

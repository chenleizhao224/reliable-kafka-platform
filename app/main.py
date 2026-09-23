"""Minimal operational API for the first delivery milestone."""

from os import getenv

from fastapi import FastAPI

app = FastAPI(
    title="Reliable Kafka Platform",
    description="Operational API for the incremental platform lab.",
    version="0.1.0",
)


@app.get("/health", tags=["operations"])
def health() -> dict[str, str]:
    """Report whether the service process is ready to receive traffic."""
    return {"status": "healthy"}


@app.get("/version", tags=["operations"])
def version() -> dict[str, str]:
    """Expose release identity so a deployment can be verified."""
    return {
        "service": "reliable-kafka-platform",
        "environment": getenv("DEPLOYMENT_ENV", "local"),
        "version": getenv("SERVICE_VERSION", "0.1.0"),
        "commit": getenv("GIT_COMMIT", "development"),
    }

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_reports_healthy() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version_has_safe_local_defaults() -> None:
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "service": "reliable-kafka-platform",
        "environment": "local",
        "version": "0.1.0",
        "commit": "development",
    }


def test_version_uses_release_environment(monkeypatch) -> None:
    monkeypatch.setenv("DEPLOYMENT_ENV", "staging")
    monkeypatch.setenv("SERVICE_VERSION", "0.1.1")
    monkeypatch.setenv("GIT_COMMIT", "abc1234")

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "service": "reliable-kafka-platform",
        "environment": "staging",
        "version": "0.1.1",
        "commit": "abc1234",
    }

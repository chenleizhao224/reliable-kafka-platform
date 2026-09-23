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


# Project Roadmap

This document outlines the planned features and improvements for the Ralph Autonomous Agent.

## Current Version: 1.0.0

Core functionality established:
- FastAPI application with `/info` endpoint
- Autonomous loop execution via `ralph.sh`
- Task queue management via `TASKS.md`
- Git integration for automatic commits

## v1.1.0 - Memory Integration

- [ ] Integrate Mem0 for episodic memory (short-term recall)
- [ ] Integrate Graphiti for semantic memory (knowledge graph)
- [ ] Add memory search before task execution
- [ ] Implement learning from successful/failed iterations

## v1.2.0 - Enhanced API

- [ ] Add `/health` endpoint for liveness checks
- [ ] Add `/tasks` endpoint to view pending tasks
- [ ] Add `/memory` endpoint to query agent memory
- [ ] Implement authentication middleware

## v1.3.0 - Multi-Agent Support

- [ ] Support for multiple concurrent Ralph instances
- [ ] Task distribution across agents
- [ ] Shared memory pool for collaborative learning

## v2.0.0 - Production Readiness

- [ ] Docker containerization
- [ ] Kubernetes deployment manifests
- [ ] Comprehensive monitoring and observability
- [ ] Rate limiting and security hardening

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose new roadmap items.

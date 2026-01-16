# Dependencies

This document describes the project's dependencies and their purposes.

## Runtime Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | latest | Modern web framework for building APIs |
| `uvicorn` | latest | ASGI server for running FastAPI |
| `fastmcp` | >=2.0.0 | MCP server framework for God Mode tools |
| `chromadb` | >=0.3.23 | Vector database for Mem0 memory layer |

## Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pytest` | latest | Testing framework |
| `httpx` | latest | HTTP client for testing (via FastAPI TestClient) |

## Installation

```bash
pip install -r requirements.txt
```

## Updating Dependencies

1. Update version in `requirements.txt`
2. Run `pip install -r requirements.txt`
3. Verify tests still pass
4. Commit changes

## Security Considerations

- Regularly update dependencies for security patches
- Use `pip audit` to check for known vulnerabilities
- Pin versions in production for reproducibility

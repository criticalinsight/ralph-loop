# System Architecture

## Overview
This project is an autonomous agent implementation using a lightweight FastAPI backend. The system is designed to be modular, testable, and easily extensible.

## Components

### 1. API Layer (`src/api.py`)
- **Framework**: FastAPI
- **Purpose**: Exposes HTTP endpoints for external interaction and monitoring.
- **Key Endpoints**:
  - `/info`: Returns system status and version information.

### 2. Testing (`tests/`)
- **Framework**: Pytest
- **Client**: HTTPX (for async API testing)
- **Strategy**: Unit tests verify endpoint availability and response schemas.

### 3. Task Management
- **TASKS.md**: The source of truth for pending work items.
- **RALPH_LOG.md**: Execution log for the autonomous agent "Ralph".

## Data Flow
1. **Request**: External client hits `/info`.
2. **Processing**: `src/api.py` handles the request logic.
3. **Response**: JSON payload returned to client.

## Directory Structure
Refer to `README.md` for the current visual representation of the project hierarchy.

## Workspace Isolation

Ralph is designed for **Self-Contained Autonomy**:
- Every project workspace maintains its own `context.txt`, `ralph_driver.py`, and `TASKS.md`.
- No cross-workspace context leakage occurs; the agent focuses entirely on the local codebase.
- Autonomous GitHub synchronization is scoped to the local repository's `origin`.
- DNA Replication: The prompt in `GEMINI.md` allows any new workspace to instantiate its own independent Ralph loop.
# Troubleshooting Guide

This guide outlines common issues encountered when running the Ralph application and their solutions.

## Common Issues

### 1. Application Fails to Start

**Symptom:** `Address already in use` error.
**Cause:** Port 8000 is occupied by another process.
**Solution:**
- Identify the process: `lsof -i :8000`
- Kill the process: `kill -9 <PID>`
- Or run on a different port: `uvicorn src.api:app --port 8001`

**Symptom:** `ModuleNotFoundError`.
**Cause:** Dependencies are missing.
**Solution:**
- Run: `pip install -r requirements.txt`

### 2. API Errors

**Symptom:** `500 Internal Server Error`.
**Cause:** Unhandled exception in the code.
**Solution:**
- Check the console logs where `uvicorn` is running for the stack trace.

### 3. Testing Issues

**Symptom:** Tests fail with `ModuleNotFoundError: No module named 'src'`.
**Cause:** Python path issues.
**Solution:**
- Run tests as a module: `python -m pytest`
- Ensure `__init__.py` exists in `src/`.

## Logs

Check `RALPH_LOG.md` for internal agent logs if the issue relates to the autonomous implementation loop.
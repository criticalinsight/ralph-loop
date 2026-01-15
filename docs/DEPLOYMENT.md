# Deployment Guide

This guide describes how to deploy the Ralph Autonomous Agent system and its underlying FastAPI application.

## Prerequisites

- Python 3.9+
- pip
- Docker (optional, for containerized deployment)

## Environment Variables

The application requires specific environment variables to function securely. Never commit `.env` files to version control.

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | The port the API listens on | `8000` |
| `ENV` | Environment (dev/prod) | `dev` |

## Local Deployment (Bare Metal)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Application**
   Use `uvicorn` to start the server:
   ```bash
   uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Verify**
   Visit `http://localhost:8000/info` to check status.

## Docker Deployment

To deploy using Docker, create a `Dockerfile` in the root directory (if one does not exist) and build the image.

1. **Build Image**
   ```bash
   docker build -t ralph-agent .
   ```

2. **Run Container**
   ```bash
   docker run -d -p 8000:8000 --name ralph-instance ralph-agent
   ```

## Cloud Deployment Options

### Heroku

1. Create a `Procfile`:
   ```text
   web: uvicorn src.api:app --host 0.0.0.0 --port $PORT
   ```
2. Push to Heroku Git remote.

### AWS / Google Cloud

Recommend using container services (AWS ECS, Google Cloud Run) by pushing the Docker image to a registry and deploying the service.

## Health Checks

Configure your load balancer or orchestration system to check:
- Endpoint: `/info`
- Expected Status: `200 OK`
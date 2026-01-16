# Contributing Guide

This document outlines how to contribute to the Ralph Autonomous Agent project.

## Getting Started

1. **Fork the Repository**: Create your own fork on GitHub
2. **Clone Locally**: `git clone <your-fork-url>`
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Create a Branch**: `git checkout -b feature/your-feature-name`

## Development Workflow

### Code Standards

- Follow PEP 8 for Python code style
- Use type hints where appropriate
- Write docstrings for all public functions
- Maintain test coverage above 80%

### Running Tests

```bash
source venv/bin/activate
python -m pytest tests/ -v
```

### Commit Messages

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/modifications
- `refactor:` for code refactoring

## Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Request review from maintainers
4. Address feedback promptly

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person

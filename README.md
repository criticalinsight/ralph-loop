# Ralph - Autonomous Implementation Agent

An autonomous coding agent that operates in a continuous feedback loop, iterating until all tasks are complete.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         ralph.sh (The Heart)                        │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  while true:                                                   │  │
│  │    1. Check TASKS.md for pending items                        │  │
│  │    2. Build context: PROMPT.md + TASKS.md + RALPH_LOG.md     │  │
│  │    3. Invoke AI agent with context                            │  │
│  │    4. Sleep and repeat                                        │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      god_mode_tools.py (The Hands)                  │
│  ┌─────────────────────┐  ┌─────────────────────┐                   │
│  │   git_save_point()  │  │ deploy_cloudflare() │                   │
│  │   git_status()      │  │ run_tests()         │                   │
│  │                     │  │ run_build()         │                   │
│  └─────────────────────┘  └─────────────────────┘                   │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        PROMPT.md (The Brain)                        │
│  • Loop Rules: Read → Act → Verify → Commit → Deploy                │
│  • Constraints: No chitchat, fail fast, one task at a time          │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Ensure your agent CLI is available (e.g., `claude`, `aider`, or your preferred tool).

```bash
# Optional: Set custom agent command
export RALPH_AGENT_CMD="your-agent-cli"
```

### 3. Initialize Git (if needed)

```bash
git init
git remote add origin <your-repo-url>
```

### 4. Add Your First Task

Edit `TASKS.md`:

```markdown
[ ] Create a simple Hello World API
[ ] Add unit tests for the API
[ ] Set up CI/CD pipeline
```

### 5. Start the Loop

```bash
chmod +x ralph.sh
./ralph.sh
```

## Files

| File | Purpose |
|------|---------|
| `PROMPT.md` | System prompt defining Ralph's behavior |
| `TASKS.md` | Task list (checkbox format) |
| `RALPH_LOG.md` | Persistent activity log (Ralph's memory) |
| `god_mode_tools.py` | MCP server with git/deploy tools |
| `ralph.sh` | Main execution loop |

## MCP Tools

| Tool | Description |
|------|-------------|
| `git_save_point(message)` | Stage, commit, and push all changes |
| `git_status()` | Check current git state |
| `deploy_to_cloudflare(project, branch)` | Deploy to Cloudflare Pages |
| `run_tests(command)` | Execute test suite |
| `run_build(command)` | Execute build command |

## Task Format

```markdown
[ ] Pending task
[/] In progress
[x] Completed
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `RALPH_AGENT_CMD` | `claude` | Agent CLI command |
| `RALPH_WORK_DIR` | Script directory | Working directory |

## License

MIT

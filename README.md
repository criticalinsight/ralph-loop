# Ralph - Autonomous Implementation Agent 🍩

An autonomous coding agent that operates in a continuous feedback loop, iterating until all tasks are complete. Ralph acts as your **"Persistent Hands"**, Bridge the gap between planning and implementation.

## Why Ralph for Antigravity & MacOS?

Ralph is specifically designed to supercharge the workflow of professional coders using the **Antigravity IDE** on a **MacBook**.

- **🚀 Autonomous Synergy:** While you use Antigravity to architect high-level plans and PRDs, Ralph handles the "manual labor." Hand off your `TASKS.md` to Ralph and watch him implement, test, and push to GitHub while you focus on the next big feature.
- **💻 MacOS-Optimized Efficiency:** Built to run as a lightweight background process on macOS, Ralph ensures that multiple autonomous loops don't bog down your MacBook's performance, leaving plenty of RAM for your development environment.
- **🛠️ Integrated "God Mode" (MCP):** Deeply integrated with the Antigravity MCP client. You can trigger Ralph's `git_save_point` or `deploy_to_cloudflare` directly from your IDE, or let Ralph call them autonomously.
- **⛓️ Continuous Sync:** Ralph excludes sensitive data (API keys) automatically and keeps your GitHub repository in constant sync. Start a feature on your Mac at the office, and your remote repo is already updated by the time you're home.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                       ralph_driver.py (The Heart)                   │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  while true:                                                   │  │
│  │    1. Check TASKS.md for pending items                        │  │
│  │    2. Call Gemini 3 Pro (Fallback: Flash)                     │  │
│  │    3. Parse & Execute: Code Blocks + Shell                    │  │
│  │    4. Safe GitHub Sync + 1hr Sleep on Rate limits             │  │
│  │    5. Loop iteration complete                                 │  │
│  │    6. Sleep and repeat                                        │  │
│  │  └────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      god_mode_tools.py (The Hands)                  │
│  ┌─────────────────────┐  ┌─────────────────────┐                   │
│  │   git_save_point()  │  │ deploy_cloudflare() │                   │
│  │   git_status()      │  │ run_tests()         │                   │
│  │                     │  │ run_build()         │                   │
│  │                     │  │                     │                   │
│  └─────────────────────┘  └─────────────────────┘                   │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        PROMPT.md (The Brain)                        │
│  • Loop Rules: Read → Act → Verify → Commit → Sync                  │
│  • Constraints: No chitchat, NEVER LEAK KEYS, Fail Fast             │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Start (The Antigravity Way)

### 1. Initialize DNA
Add the **Ralph Autonomy Protocol** to your project using the blueprint prompt in your `GEMINI.md`.

### 2. Configure Environment
Ralph uses `llm-gemini` for high-speed, reliable iterations.
```bash
source venv/bin/activate
export GEMINI_API_KEY="AIzaSy..."
```

### 3. Start the Heart
```bash
./ralph.sh
```

## Global MCP Integration (Antigravity IDE)

To use Ralph's "God Mode" tools globally across your IDE, add the following server definition to your `mcp_config.json` (typically at `~/.antigravity/mcp_config.json` or within your Claude Desktop config):

```json
"ralph-god-mode": {
  "command": "/Users/x/Documents/mac/loop/venv/bin/python",
  "args": [
    "/Users/x/Documents/mac/loop/god_mode_tools.py"
  ],
  "cwd": "/Users/x/Documents/mac/loop",
  "env": {
    "GEMINI_API_KEY": "YOUR_API_KEY_HERE"
  }
}
```

### Installation Steps:
1. Ensure the Python `venv` in this project is initialized and has `fastmcp` installed.
2. Update the `command` and `args` paths in the JSON above to match your absolute local paths.
3. Restart your Antigravity MCP client to activate the tools.

## Features for High-Power Coders

- **Model Hierarchy:** Prioritizes `gemini-3-pro-preview` for complex logic, falling back to `gemini-3-flash-preview` for speed.
- **API Safety:** Automated 1-hour "Cool Down" if rate limits are hit, essential for long-running MacBook sessions.
- **Security First:** The driver performs a `git diff` scan for Google AI keys before every push, guaranteeing no sensitive leaks to public repos.

## MCP Tools (Native to Antigravity)

| Tool | Action |
|------|--------|
| `git_save_point` | Full git cycle: Add → Commit → Push |
| `run_tests` | Automated verification before syncing |
| `deploy_to_cloudflare` | One-click deployment once tasks are [x] |

---
*Created with Antigravity — The future of autonomous coding on macOS.*

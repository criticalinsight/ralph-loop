# god_tools.py
import subprocess
import os
from fastmcp import FastMCP

# Initialize the MCP Server
mcp = FastMCP("Ralph-God-Mode-Tools")

@mcp.tool()
def git_save_point(message: str) -> str:
    """
    STAGES, COMMITS, and PUSHES all current changes.
    Use this when a task is completed successfully.
    """
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Ralph: {message}"], check=True)
        subprocess.run(["git", "push"], check=True)
        return "✅ Saved to GitHub."
    except Exception as e:
        return f"❌ Git failed: {str(e)}"

@mcp.tool()
def deploy_to_cloudflare(project_name: str) -> str:
    """
    Triggers a Cloudflare Pages deployment via Wrangler.
    Only use when TASKS.md is fully complete.
    """
    try:
        # Assumes 'wrangler' is installed via npm
        cmd = ["npx", "wrangler", "pages", "deploy", ".", "--project-name", project_name]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return f"🚀 DEPLOYED: {result.stdout}"
        else:
            return f"🔥 FAILED: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()

# god_mode_tools.py
"""
Ralph MCP Server - "The Hands"
Provides high-power tools for autonomous git operations and Cloudflare deployment.
"""
import subprocess
import os
from datetime import datetime
from fastmcp import FastMCP

# Initialize the MCP Server
mcp = FastMCP("Ralph-God-Mode-Tools")


@mcp.tool()
def git_save_point(message: str) -> str:
    """
    STAGES, COMMITS, and PUSHES all current changes.
    Use this when a task is completed successfully.
    
    Args:
        message: Commit message describing the changes made
    
    Returns:
        Success or error message
    """
    try:
        # 1. Add all changes
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        
        # 2. Commit with Ralph prefix
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        commit_msg = f"Ralph [{timestamp}]: {message}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)
        
        # 3. Push (Assumes SSH keys are configured)
        subprocess.run(["git", "push"], check=True, capture_output=True)
        
        return f"✅ Success: Committed and pushed - '{message}'"
    
    except subprocess.CalledProcessError as e:
        error_output = e.stderr.decode() if e.stderr else str(e)
        return f"❌ Git Error: {error_output}"


@mcp.tool()
def git_status() -> str:
    """
    Returns the current git status.
    Use this to check for uncommitted changes before committing.
    
    Returns:
        Git status output
    """
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout.strip():
            return f"📋 Modified files:\n{result.stdout}"
        return "✅ Working tree clean"
    except subprocess.CalledProcessError as e:
        return f"❌ Git Error: {e.stderr}"


@mcp.tool()
def deploy_to_cloudflare(project_name: str, branch: str = "main", directory: str = ".") -> str:
    """
    Triggers a Cloudflare Pages/Workers deployment via Wrangler.
    Use this ONLY when all tasks in TASKS.md are complete.
    
    Args:
        project_name: The Cloudflare Pages project name
        branch: Git branch to deploy (default: main)
        directory: Directory to deploy (default: current directory)
    
    Returns:
        Deployment result with URL or error message
    """
    try:
        cmd = [
            "npx", "wrangler", "pages", "deploy", directory,
            "--project-name", project_name,
            "--branch", branch
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            return f"🚀 DEPLOYMENT SUCCESSFUL:\n{result.stdout}"
        else:
            return f"🔥 DEPLOYMENT FAILED:\n{result.stderr}"
            
    except subprocess.TimeoutExpired:
        return "🔥 DEPLOYMENT TIMEOUT: Process exceeded 5 minute limit"
    except Exception as e:
        return f"🔥 CRITICAL ERROR: {str(e)}"


@mcp.tool()
def run_tests(command: str = "npm test") -> str:
    """
    Runs the project test suite.
    Use this to verify code before committing.
    
    Args:
        command: Test command to execute (default: npm test)
    
    Returns:
        Test results or error message
    """
    try:
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            return f"✅ TESTS PASSED:\n{result.stdout[-2000:]}"  # Last 2000 chars
        else:
            return f"❌ TESTS FAILED:\n{result.stderr[-2000:]}"
            
    except subprocess.TimeoutExpired:
        return "❌ TEST TIMEOUT: Tests exceeded 2 minute limit"
    except Exception as e:
        return f"❌ TEST ERROR: {str(e)}"


@mcp.tool()
def run_build(command: str = "npm run build") -> str:
    """
    Runs the project build command.
    Use this to verify the code compiles before committing.
    
    Args:
        command: Build command to execute (default: npm run build)
    
    Returns:
        Build result or error message
    """
    try:
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            timeout=180
        )
        
        if result.returncode == 0:
            return f"✅ BUILD SUCCESSFUL:\n{result.stdout[-1000:]}"
        else:
            return f"❌ BUILD FAILED:\n{result.stderr[-2000:]}"
            
    except subprocess.TimeoutExpired:
        return "❌ BUILD TIMEOUT: Build exceeded 3 minute limit"
    except Exception as e:
        return f"❌ BUILD ERROR: {str(e)}"


if __name__ == "__main__":
    print("🤖 Starting Ralph God Mode Tools MCP Server...")
    mcp.run()

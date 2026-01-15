# ralph_driver.py
import os
import re
import subprocess
import sys
import time

def run_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout + result.stderr

def extract_code_blocks(text):
    blocks = []
    # Pattern to match: ```lang [path]
    # content
    # ```
    pattern = r"```(?:[\w\.]+)?\s*(\S+)?\n(.*?)\n```"
    matches = re.finditer(pattern, text, re.DOTALL)
    for match in matches:
        path = match.group(1)
        content = match.group(2)
        
        # If no path was in the ``` block, check for a filename in the first few lines of content
        if not path or path == "":
             # Look for # filename.py or // filename.js in the first two lines
             first_lines = content.split("\n")[:2]
             for line in first_lines:
                 m = re.search(r"(?:#|//|<!--)\s*([\w\./\-]+\.\w+)", line)
                 if m:
                     path = m.group(1)
                     break

        if path and "." in path and path.lower() != "python" and path.lower() != "bash":
            blocks.append((path, content))
        elif "apt-get" in content or "pip install" in content or "git " in content or "npx " in content:
            blocks.append(("SHELL", content))
        elif path and path.lower() in ["bash", "sh", "shell", "zsh"]:
            blocks.append(("SHELL", content))
            
    return blocks

def call_llm(model, context_file):
    print(f"Calling Gemini ({model})...")
    llm_cmd = f"source venv/bin/activate && cat {context_file} | llm prompt -m {model}"
    result = subprocess.run(llm_cmd, shell=True, capture_output=True, text=True, executable="/bin/zsh")
    return result

def is_rate_limited(result):
    error_msg = result.stderr.lower()
    return "429" in error_msg or "rate limit" in error_msg

def git_sync():
    """Safety check and push to GitHub"""
    print("Starting GitHub sync...")
    
    # 1. Check for API keys in staged changes
    # Added files and modifications
    staged_diff = subprocess.run("git diff --cached", shell=True, capture_output=True, text=True).stdout
    key_pattern = r"AIzaSy[A-Za-z0-9-_]{33}"
    
    if re.search(key_pattern, staged_diff):
        print("CRITICAL: Detected potential API key in staged changes! Aborting push.")
        return False

    # 2. Add, commit, and push
    subprocess.run("git add .", shell=True)
    
    # Check if there are changes to commit
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True).stdout
    if status:
        print("Committing changes...")
        subprocess.run('git commit -m "Ralph: Autonomous update and documentation"', shell=True)
        print("Pushing to GitHub...")
        push_result = subprocess.run("git push origin main", shell=True, capture_output=True, text=True)
        if push_result.returncode == 0:
            print("Successfully pushed to GitHub.")
        else:
            print(f"Error pushing to GitHub: {push_result.stderr}")
    else:
        print("No changes to sync.")
    return True

def main():
    if not os.path.exists("context.txt"):
        print("Error: context.txt not found")
        return

    primary_model = "gemini-3-pro-preview"
    fallback_model = "gemini-3-flash-preview"
    
    # 1. Try Primary Model
    result = call_llm(primary_model, "context.txt")
    
    if is_rate_limited(result):
        print(f"Warning: Primary model ({primary_model}) rate limited.")
        # 2. Try Fallback Model
        result = call_llm(fallback_model, "context.txt")
        
        if is_rate_limited(result):
            print(f"CRITICAL: Both models rate limited. Sleeping for 1 hour...")
            time.sleep(3600)
            return

    if result.returncode != 0:
        print(f"Error calling LLM: {result.stderr}")
        return

    response = result.stdout
    print("\n--- AGENT RESPONSE ---\n")
    print(response)
    print("\n--- END RESPONSE ---\n")

    # 3. Extract and execute actions
    actions = extract_code_blocks(response)
    
    for path, content in actions:
        if path == "SHELL":
            print(f"Running shell command...")
            run_command(content)
        else:
            print(f"Writing file: {path}")
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)

    # 4. Handle status updates
    if "task is complete" in response.lower() or "[x]" in response:
        print("Agent indicates task completion. Updating TASKS.md...")
        try:
            with open("TASKS.md", "r") as f:
                content = f.read()
            new_content = re.sub(r"\[ \]", "[x]", content, count=1)
            if new_content != content:
                with open("TASKS.md", "w") as f:
                    f.write(new_content)
                print("Successfully checked off task in TASKS.md")
        except Exception as e:
            print(f"Error updating TASKS.md: {e}")

    # 5. ALWAYS SYNC TO GITHUB
    git_sync()

if __name__ == "__main__":
    main()

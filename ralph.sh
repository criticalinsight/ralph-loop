#!/bin/bash
# ralph.sh - The Autonomy Loop
#
# Adapted to use 'llm' with 'llm-gemini' due to Python 3.14 incompatibilities.

# Configuration
# Note: Ensure you have your Google API key exported as GEMINI_API_KEY
# Model prioritization and rate limiting are handled by ralph_driver.py
# (gemini-3-pro-preview -> gemini-3-flash-preview | sleep 1hr on 429)
MCP_SERVER="python god_tools.py"

echo "🍩 Starting Ralph Loop (llm-gemini version). Press Ctrl+C to stop."

# Ensure we are in the venv
if [ -z "$VIRTUAL_ENV" ]; then
  source venv/bin/activate
fi

while true; do
  # 2. CHECK QUEUE
  if grep -q "\[ \]" TASKS.md; then
    
    # 3. BUILD CONTEXT PACKET
    echo "--- INSTRUCTIONS ---" > context.txt
    cat PROMPT.md >> context.txt
    echo -e "\n--- TASKS ---" >> context.txt
    cat TASKS.md >> context.txt
    echo -e "\n--- RECENT LOGS ---" >> context.txt
    tail -n 15 RALPH_LOG.md >> context.txt
    
    # 4. EXECUTE THE AGENT
    # Use the custom driver to handle the API call and code execution
    python3 ralph_driver.py >> RALPH_LOG.md 2>&1
    
    # 5. LOG & SLEEP
    echo "$(date): Loop iteration complete." >> RALPH_LOG.md
    sleep 5
    
  else
    echo "🎉 All tasks done. Ralph is sleeping."
    sleep 60
  fi
done

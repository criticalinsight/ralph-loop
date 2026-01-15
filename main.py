import os

def create_initial_files():
    """
    Creates the initial files required for the Ralph autonomous agent system.
    """

    # Create TASKS.md if it doesn't exist
    if not os.path.exists("TASKS.md"):
        with open("TASKS.md", "w") as f:
            f.write("# Tasks\n\n")
            f.write("<!-- \n")
            f.write("Task Format:\n")
            f.write("[ ] = Pending task\n")
            f.write("[/] = In progress\n")
            f.write("[x] = Completed\n\n")
            f.write("Add your tasks below. Ralph will process them top-to-bottom.\n")
            f.write("-->\n\n")
            f.write("[ ] Initialize the Ralph autonomous agent system\n") # Put the original task back

    # Create RALPH_LOG.md if it doesn't exist
    if not os.path.exists("RALPH_LOG.md"):
        with open("RALPH_LOG.md", "w") as f:
            f.write("--- RECENT LOGS ---\n")

def initialize_ralph():
    """
    Initializes the Ralph autonomous agent system by creating necessary files.
    """
    create_initial_files()


if __name__ == "__main__":
    initialize_ralph()
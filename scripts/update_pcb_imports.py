import subprocess
import sys
import os

PROJECT_PATH = "pcb-template-project/"
SUBMODULE_PATH = os.path.join(PROJECT_PATH, "PCB-Imports")   # REPLACE with your submodule path
PROJECT_SCRIPT = "./scripts/update-lib-tables.py"            # REPLACE with your file update script

def run_git_command(command):
    """Executes a git command and prints output on failure."""
    try:
        subprocess.run(command, check=True, text=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(command)}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        return False

def update_submodules():
    """Update the submodule to the commit recorded in the index."""
    print("1. Updating submodules...")
    # This command updates the submodule working directory to the commit recorded in HEAD
    if run_git_command(["git", "submodule", "update", "--init", "--recursive", SUBMODULE_PATH]):
        print("Submodule update successful.")
        return True
    return False

def update_project_files():
    """Runs the secondary script to update dependent project files."""
    print(f"2. Running project file update script: {PROJECT_SCRIPT}")
    try:
        # Run your shell script (or other program)
        subprocess.run([PROJECT_SCRIPT], check=True)
        print("Project files updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Invoked subprocess.CalledProcessError:\n{e}\n")
        print(f"Project update script failed: {PROJECT_SCRIPT}", file=sys.stderr)
        sys.exit(1) # Exit if the core update fails

if __name__ == "__main__":
    # Change directory to the repository root before running commands
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

    if update_submodules():
        update_project_files()

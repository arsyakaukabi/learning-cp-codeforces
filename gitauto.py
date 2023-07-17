import subprocess

commit_message = "Added new solutions"
try:
    subprocess.run(
        ["git", "add", "."], check=True
    )  # Add all changes to the staging area
    subprocess.run(
        ["git", "commit", "-m", commit_message], check=True
    )  # Commit changes with the provided message
    subprocess.run(
        ["git", "push", "origin", "main"], check=True
    )  # Push changes to the origin main branch
    print("Commit and push successful!")
except subprocess.CalledProcessError as e:
    print("Commit and push failed. Error:", e)

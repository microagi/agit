import json
import os
from git import Repo, GitCommandError, InvalidGitRepositoryError
from pathlib import Path


def get_repo_status(repo):
    """Get the current status of the repository."""
    return repo.git.status()


def get_branch_info(repo):
    """Get information about the branches."""
    branches = repo.branches
    return [str(branch) for branch in branches]


def get_commit_history(repo, limit=10):
    """Get the commit history, limited to the most recent 'limit' commits."""
    commits = list(repo.iter_commits('HEAD', max_count=limit))
    return [{"hash": commit.hexsha, "author": commit.author.name, "summary": commit.summary} for commit in commits]


def get_conflict_info(repo):
    """Get information about any merge conflicts."""
    # Checking index for merge conflicts
    conflicted_files = [path for path, entry in repo.index.entries.items() if entry.stage != 0]
    return conflicted_files if conflicted_files else "No conflicts"


def find_git_repo(start):
    """Finds the .git directory in the current or parent directories."""
    current_dir = Path(start).resolve()
    for parent in [current_dir, *current_dir.parents]:
        if any(folder.name == '.git' for folder in parent.iterdir() if folder.is_dir()):
            return str(parent)
    return None


def retrieve_git_data(start_path):
    """Retrieve a summary of the git repository data."""
    repo_path = find_git_repo(start_path)
    if not repo_path:
        return "Error: No git repository found in the current or parent directories."

    try:
        repo = Repo(repo_path)
    except (GitCommandError, InvalidGitRepositoryError):
        return "Error: Not a git repository or no access to repository."

    data = {
        "status": get_repo_status(repo),
        "branches": get_branch_info(repo),
        "recent_commits": get_commit_history(repo),
        "conflicts": get_conflict_info(repo)
    }

    return data


if __name__ == "__main__":
    r_path = '.'  # Set the path to your git repository
    git_data = retrieve_git_data(r_path)
    print(json.dumps(git_data, indent=4))

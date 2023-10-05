# Copyright (C) 2023 Sivan Grünberg <sivan@vitakka.co>
# Vitakka Consulting https://vitakka.co
#
# The microAGI tool AGit is open sourced under GPLv3 license.
#
# If you find it useful, we would greatly appreciate a symbolic contribution to
# acknowledge the value and effort behind the project.
# As a guideline, we'd appreciate a contribution equivalent to $10 via GitHub Sponsors,
# Your support helps us continue to provide and improve this tool for everyone!
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.


DESTRUCTIVE_COMMANDS = {
    "push --force": "Force pushes can overwrite remote branches, potentially discarding commits.",
    "push -f": "Shortened version of 'git push --force'.",
    "branch -D": "Force deletes a branch, regardless of its merged status.",
    "branch -d": "Deletes a branch. Not generally destructive, but included for completeness.",
    "checkout -B": "Creates a new branch or resets an existing branch to a start point. Could overwrite work on existing branches.",
    "checkout -b": "Creates a new branch. Not generally destructive, but included for completeness.",
    "clean -fd": "Force deletes untracked files and directories in the working copy, potentially erasing work.",
    "clean -f": "Force deletes untracked files in the working copy, potentially erasing work.",
    "reset --hard": "Resets the index and working tree to match a specified commit. Any changes to tracked files in the working tree since the specified commit are lost.",
    "reset --soft": "Moves the HEAD to a specified commit. Changes since the specified commit are kept. Can be destructive if not handled properly.",
    "reset --mixed": "Resets the index but not the working tree and reports what has not been updated.",
    "rebase": "Applies your changes on top of another base tip, which can create conflicts.",
    "rm --cached": "Unstages and removes paths only from the index (not the working tree) and can cause loss of work.",
    "rm": "Removes files from the working tree and from the index.",
    "stash clear": "Removes all stashed entries, potentially erasing saved work.",
    "stash drop": "Removes a single stash entry, potentially erasing saved work.",
    "commit --amend": "Modifies the last commit, which can be dangerous if that commit has already been pushed.",
    "merge": "Combines changes from multiple branches. Not generally destructive, but can create conflicts if not handled properly.",
    "fsck --full": "Verifies the connectivity and validity of the objects in the database, which can expose issues.",
    "gc --prune=now": "Cleans up unnecessary files and optimizes your local repository, but can remove objects not yet merged into the base branch.",
    "reflog expire --expire=now --all": "Removes 'older' entries from reflog, potentially making it harder to recover from mistakes.",
    "update-ref -d": "Deletes a ref, potentially making it harder to find or recover that reference point.",
    "filter-branch": "Rewrites Git history, applying a filter expression to each commit, which can alter commit hashes and cause discrepancies in repository versions and may lead to loss of commit history.",
    "filter-repo": "A faster and more flexible replacement for git filter-branch, used for rewriting Git repository history. Can be destructive due to potential loss of commits, tags, and other Git objects.",
}


porcelain_commands = [
    "add",
    "am",
    "archive",
    "bisect",
    "branch",
    "bundle",
    "checkout",
    "cherry-pick",
    "citool",
    "clean",
    "clone",
    "commit",
    "describe",
    "diff",
    "fetch",
    "gc",
    "grep",
    "gui",
    "init",
    "log",
    "merge",
    "mv",
    "notes",
    "pull",
    "push",
    "range-diff",
    "rebase",
    "restore",
    "reset",
    "revert",
    "rm",
    "shortlog",
    "show",
    "stash",
    "status",
    "submodule",
    "tag",
    "worktree",
]


ALLOWED_GIT_COMMANDS = ["git"] + porcelain_commands + ['sort']

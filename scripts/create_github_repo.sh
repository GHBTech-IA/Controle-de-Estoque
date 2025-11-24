#!/usr/bin/env bash
# Create GitHub repo and push current project using GitHub CLI (gh).
# Usage: ./create_github_repo.sh [repo-name] [public|private]

set -euo pipefail

REPO_NAME=${1:-$(basename "$(pwd)")}
VISIBILITY=${2:-public}

if ! command -v git >/dev/null 2>&1; then
  echo "git is not installed. Install Git first." >&2
  exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is not installed. Install from https://cli.github.com/" >&2
  exit 1
fi

# Ensure gh is authenticated
if ! gh auth status >/dev/null 2>&1; then
  echo "You are not authenticated with gh. Running 'gh auth login'..."
  gh auth login
fi

if [ ! -d .git ]; then
  git init
  git add -A
  git commit -m "Initial commit"
fi

echo "Creating GitHub repo '$REPO_NAME' (visibility: $VISIBILITY) and pushing..."
gh repo create "$REPO_NAME" --"$VISIBILITY" --source=. --remote=origin --push

echo "Done. Repository created and pushed."

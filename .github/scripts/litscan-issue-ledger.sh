#!/usr/bin/env bash
# Read all issues, including closed and unlabelled ones. GraphQL excludes PRs.
set -euo pipefail
gh api graphql --paginate -F owner="${GITHUB_REPOSITORY%/*}" -F repo="${GITHUB_REPOSITORY#*/}" \
  -f query='query ($owner: String!, $repo: String!, $endCursor: String) {
    repository(owner: $owner, name: $repo) {
      issues(first: 100, after: $endCursor) {
        nodes { title body }
        pageInfo { hasNextPage endCursor }
      }
    }
  }' --jq '.data.repository.issues.nodes[]' | jq -s .

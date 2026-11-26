#!/bin/sh
# Run one AGENT_REVIEW gene in its sandbox with headless Claude Code.
#   sh run_agent_review.sh SANDBOX_ROOT GENE ACC MODEL EFFORT BUDGET_USD
# Writes SANDBOX_ROOT/GENE/transcript.jsonl (stream-json; the last line carries
# total_cost_usd). The API key comes from GO_ANTHROPIC_API_KEY. --bare skips the user's CLAUDE.md, hooks, plugins and memory;
# web tools and MCP servers are disabled.
set -e
unset CDPATH
ROOT=$1; GENE=$2; ACC=$3; MODEL=$4; EFFORT=$5; BUDGET=$6
HERE=$(cd "$(dirname "$0")" && pwd)
export AIGR_REPO=$(cd "$HERE/../../.." && pwd)
BOX="$ROOT/$GENE"
PROMPT=$(sed -e "s/{GENE}/$GENE/g" -e "s/{ACC}/$ACC/g" -e "s/{BASELINE}/2025-06-01/g" \
  -e "s/{BASELINE_YEAR}/2025/g" "$HERE/agent-review-prompt.md")
cd "$BOX"
ANTHROPIC_API_KEY="$GO_ANTHROPIC_API_KEY" claude -p "$PROMPT" --bare --model "$MODEL" --effort "$EFFORT" \
  --tools "Bash,Read,Write,Edit,Glob,Grep" --disallowedTools "WebSearch,WebFetch" \
  --strict-mcp-config --permission-mode bypassPermissions \
  --max-budget-usd "$BUDGET" --no-session-persistence \
  --output-format stream-json --verbose > transcript.jsonl
grep '"type":"result"' transcript.jsonl | tail -1 | python3 -c "import json,sys;r=json.load(sys.stdin);print('$GENE', r.get('subtype'), round(r.get('total_cost_usd',0),2), r.get('num_turns'))"

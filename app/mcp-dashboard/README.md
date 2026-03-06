# Gene Review Dashboard MCP App

A stateless MCP App rendering gateway. The server has **no filesystem access** and no knowledge of genes or YAML files. Instead, the AI agent computes stats locally and passes them as tool input. The server renders them as an interactive HTML dashboard inline in the chat.

## Architecture

```
You: "show me the dashboard"
  |
Agent (in sandbox): scans YAML files, computes stats
  |
Agent calls tool: gene-review-dashboard({ total_genes: 1127, action_counts: {...}, ... })
  |
MCP App server (deployed): receives stats, returns bundled HTML
  |
Claude UI: renders interactive dashboard inline in chat
```

## Local development

```bash
npm install
npm run build   # bundles HTML+JS into dist/mcp-app.html
npm run serve   # starts MCP server on port 3456
```

## Deploy

```bash
docker build -t gene-review-dashboard .
docker run -p 3456:3456 gene-review-dashboard
```

Or deploy to any container host (Railway, Fly.io, Render, etc.).

Then add the public URL as a **custom connector** in Claude Settings > Connectors.

## Tool schema

The `gene-review-dashboard` tool accepts:

```json
{
  "total_genes": 1127,
  "total_annotations": 50572,
  "total_species": 74,
  "action_counts": {
    "ACCEPT": 25292,
    "KEEP_AS_NON_CORE": 8068,
    "MODIFY": 2157,
    "REMOVE": 3460,
    "MARK_AS_OVER_ANNOTATED": 2697,
    "UNDECIDED": 472,
    "NEW": 1109,
    "PENDING": 7317
  },
  "species_gene_counts": {
    "human": 490,
    "yeast": 118,
    "worm": 109
  }
}
```

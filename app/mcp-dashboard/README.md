# Gene Review Dashboard MCP App

A lightweight MCP App server that renders an interactive gene review dashboard inline in Claude and other MCP App-compatible hosts.

## Setup

```bash
cd app/mcp-dashboard
npm install
npm run build   # bundles HTML+JS into dist/mcp-app.html
npm run serve   # starts MCP server on port 3456
```

## Connecting to Claude

For local development, expose the server via tunnel:

```bash
npx cloudflared tunnel --url http://localhost:3456
```

Then add the tunnel URL as a custom connector in Claude (Settings > Connectors > Add custom connector).

## What it shows

- Total genes, annotations, and species counts
- Bar chart of annotations by review action (Accept, Modify, Remove, etc.)
- Top species by gene count
- Refresh button to re-scan YAML files

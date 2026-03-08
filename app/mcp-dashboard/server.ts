/**
 * Stateless MCP App rendering gateway.
 *
 * This server has NO filesystem access and NO knowledge of genes/YAML.
 * The agent computes stats locally and passes them as tool input.
 * The server just renders the data as an interactive HTML dashboard.
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";
import cors from "cors";
import express from "express";
import fs from "node:fs/promises";
import path from "node:path";

const RESOURCE_MIME_TYPE = "text/html;profile=mcp-app";

// ── MCP Server ──────────────────────────────────────────────────────────

const server = new McpServer({
  name: "Gene Review Dashboard",
  version: "1.0.0",
});

const DASHBOARD_URI = "ui://gene-review-dashboard/mcp-app.html";

// The agent passes stats as input; the server just renders them
server.registerTool(
  "gene-review-dashboard",
  {
    title: "Gene Review Dashboard",
    description:
      "Renders an interactive dashboard showing gene annotation review status. " +
      "The caller provides pre-computed stats (action counts, species counts, totals). " +
      "Returns an interactive UI with bar charts and summary cards.",
    inputSchema: {
      total_genes: z.number().describe("Total number of genes reviewed"),
      total_annotations: z.number().describe("Total number of annotations"),
      total_species: z.number().describe("Total number of species"),
      action_counts: z
        .record(z.string(), z.number())
        .describe("Map of action type (ACCEPT, MODIFY, REMOVE, etc.) to count"),
      species_gene_counts: z
        .record(z.string(), z.number())
        .describe("Map of species code to gene count (top N)"),
    },
    _meta: { ui: { resourceUri: DASHBOARD_URI } },
  },
  async (args) => {
    // Pass the stats straight through as the tool result for the UI to render
    return {
      content: [{ type: "text", text: JSON.stringify(args) }],
    };
  },
);

// Serve the bundled HTML
server.resource(
  "dashboard-ui",
  DASHBOARD_URI,
  { mimeType: RESOURCE_MIME_TYPE },
  async () => {
    const html = await fs.readFile(
      path.join(import.meta.dirname, "dist", "mcp-app.html"),
      "utf-8",
    );
    return {
      contents: [{ uri: DASHBOARD_URI, mimeType: RESOURCE_MIME_TYPE, text: html }],
    };
  },
);

// ── HTTP transport ──────────────────────────────────────────────────────

const app = express();
app.use(cors());
app.use(express.json());

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined,
    enableJsonResponse: true,
  });
  res.on("close", () => transport.close());
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

const PORT = Number(process.env.PORT ?? 3456);

app.listen(PORT, () => {
  console.log(`Gene Review Dashboard MCP server listening on http://localhost:${PORT}/mcp`);
});

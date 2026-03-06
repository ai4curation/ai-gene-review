/**
 * MCP App server for gene review dashboard.
 * Reads all *-ai-review.yaml files and serves an interactive summary.
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import cors from "cors";
import express from "express";
import fs from "node:fs/promises";
import path from "node:path";
import yaml from "js-yaml";
import { glob } from "glob";

const RESOURCE_MIME_TYPE = "text/html;profile=mcp-app";

// Resolve the gene review repo root (two levels up from app/mcp-dashboard/)
const REPO_ROOT = path.resolve(import.meta.dirname, "..", "..");
const GENES_DIR = path.join(REPO_ROOT, "genes");

interface ReviewStats {
  total_genes: number;
  total_annotations: number;
  total_species: number;
  action_counts: Record<string, number>;
  species_gene_counts: Record<string, number>;
}

async function collectStats(): Promise<ReviewStats> {
  const actionCounts: Record<string, number> = {};
  const speciesGeneCounts: Record<string, number> = {};
  let totalAnnotations = 0;

  const files = await glob("**/*-ai-review.yaml", { cwd: GENES_DIR });

  for (const file of files) {
    const parts = file.split(path.sep);
    const species = parts[0] ?? "unknown";
    speciesGeneCounts[species] = (speciesGeneCounts[species] ?? 0) + 1;

    try {
      const content = await fs.readFile(path.join(GENES_DIR, file), "utf-8");
      const data = yaml.load(content) as Record<string, unknown> | null;

      if (data?.existing_annotations && Array.isArray(data.existing_annotations)) {
        for (const ann of data.existing_annotations) {
          totalAnnotations++;
          const review = (ann as Record<string, unknown>)?.review as
            | Record<string, unknown>
            | undefined;
          const action = review?.action
            ? String(review.action)
            : review
              ? "PENDING"
              : "NO_REVIEW";
          actionCounts[action] = (actionCounts[action] ?? 0) + 1;
        }
      }
    } catch {
      // skip unparseable files
    }
  }

  // Sort species by count descending, take top 20
  const sorted = Object.entries(speciesGeneCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 20);
  const topSpecies = Object.fromEntries(sorted);

  return {
    total_genes: Object.values(speciesGeneCounts).reduce((a, b) => a + b, 0),
    total_annotations: totalAnnotations,
    total_species: Object.keys(speciesGeneCounts).length,
    action_counts: actionCounts,
    species_gene_counts: topSpecies,
  };
}

// ── MCP Server ──────────────────────────────────────────────────────────

const server = new McpServer({
  name: "Gene Review Dashboard",
  version: "1.0.0",
});

const DASHBOARD_URI = "ui://gene-review-dashboard/mcp-app.html";

// Register the dashboard tool with UI metadata
server.registerTool(
  "gene-review-dashboard",
  {
    title: "Gene Review Dashboard",
    description:
      "Shows an interactive dashboard summarizing annotation review status across all genes. " +
      "Displays total counts, breakdown by review action, and top species.",
    _meta: { ui: { resourceUri: DASHBOARD_URI } },
  },
  async () => {
    const stats = await collectStats();
    return {
      content: [{ type: "text", text: JSON.stringify(stats) }],
    };
  },
);

// Register the UI resource that serves the bundled HTML
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

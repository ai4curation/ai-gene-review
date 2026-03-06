import { App } from "@modelcontextprotocol/ext-apps";

const contentEl = document.getElementById("content")!;

const ACTION_COLORS: Record<string, string> = {
  ACCEPT: "#22c55e",
  KEEP_AS_NON_CORE: "#60a5fa",
  MODIFY: "#f59e0b",
  REMOVE: "#ef4444",
  MARK_AS_OVER_ANNOTATED: "#f97316",
  UNDECIDED: "#a78bfa",
  NEW: "#06b6d4",
  PENDING: "#94a3b8",
  NO_REVIEW: "#cbd5e1",
};

const ACTION_ORDER = [
  "ACCEPT",
  "KEEP_AS_NON_CORE",
  "MODIFY",
  "REMOVE",
  "MARK_AS_OVER_ANNOTATED",
  "UNDECIDED",
  "NEW",
  "PENDING",
  "NO_REVIEW",
];

interface Stats {
  total_genes: number;
  total_annotations: number;
  total_species: number;
  action_counts: Record<string, number>;
  species_gene_counts: Record<string, number>;
}

function fmt(n: number): string {
  return n.toLocaleString();
}

function renderDashboard(stats: Stats) {
  const actions = stats.action_counts;
  const maxCount = Math.max(...Object.values(actions), 1);

  const barRows = ACTION_ORDER.filter((a) => (actions[a] ?? 0) > 0)
    .map((action) => {
      const count = actions[action] ?? 0;
      const pct = ((count / maxCount) * 100).toFixed(1);
      const color = ACTION_COLORS[action] ?? "#94a3b8";
      const label = action.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
      return `
        <div class="bar-row">
          <div class="bar-label">${label}</div>
          <div class="bar-track">
            <div class="bar-fill" style="width:${pct}%;background:${color}"></div>
          </div>
          <div class="bar-count">${fmt(count)}</div>
        </div>`;
    })
    .join("");

  const speciesRows = Object.entries(stats.species_gene_counts)
    .map(([sp, count]) => `<tr><td>${sp}</td><td>${count}</td></tr>`)
    .join("");

  contentEl.innerHTML = `
    <div class="stats-row">
      <div class="stat-card"><div class="stat-value">${fmt(stats.total_genes)}</div><div class="stat-label">Genes</div></div>
      <div class="stat-card"><div class="stat-value">${fmt(stats.total_annotations)}</div><div class="stat-label">Annotations</div></div>
      <div class="stat-card"><div class="stat-value">${stats.total_species}</div><div class="stat-label">Species</div></div>
      <div class="stat-card"><div class="stat-value">${fmt(actions["ACCEPT"] ?? 0)}</div><div class="stat-label">Accepted</div></div>
    </div>
    <div class="card">
      <h2>Annotations by Review Action</h2>
      ${barRows}
    </div>
    <div class="card">
      <h2>Top Species by Gene Count</h2>
      <table>
        <thead><tr><th>Species</th><th>Genes</th></tr></thead>
        <tbody>${speciesRows}</tbody>
      </table>
    </div>`;
}

function parseStats(result: { content?: Array<{ type: string; text?: string }> }): Stats | null {
  const text = result.content?.find((c) => c.type === "text")?.text;
  if (!text) return null;
  try {
    return JSON.parse(text) as Stats;
  } catch {
    return null;
  }
}

// ── MCP App communication ───────────────────────────────────────────────

const app = new App({ name: "Gene Review Dashboard", version: "1.0.0" });
app.connect();

// The host pushes the tool result (stats computed by the agent) to the UI
app.ontoolresult = (result) => {
  const stats = parseStats(result);
  if (stats) {
    renderDashboard(stats);
  } else {
    contentEl.innerHTML = '<div class="loading">Could not parse stats.</div>';
  }
};

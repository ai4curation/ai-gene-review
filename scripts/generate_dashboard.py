#!/usr/bin/env python3
"""Generate a self-contained HTML dashboard summarizing gene review status."""

import yaml
import glob
import collections
import json
import sys
from pathlib import Path


def collect_stats(base_dir: str = "genes"):
    action_counts = collections.Counter()
    species_gene_counts = collections.Counter()
    species_annotation_counts = collections.Counter()
    total_annotations = 0

    for f in sorted(glob.glob(f"{base_dir}/**/*-ai-review.yaml", recursive=True)):
        parts = Path(f).parts
        species = parts[1] if len(parts) > 2 else "unknown"
        species_gene_counts[species] += 1

        try:
            with open(f) as fh:
                data = yaml.safe_load(fh)
            if data and "existing_annotations" in data and data["existing_annotations"]:
                for ann in data["existing_annotations"]:
                    total_annotations += 1
                    species_annotation_counts[species] += 1
                    review = ann.get("review", {})
                    if review:
                        action = review.get("action", "PENDING")
                        action_counts[action] += 1
                    else:
                        action_counts["NO_REVIEW"] += 1
        except Exception:
            pass

    return {
        "action_counts": dict(action_counts),
        "species_gene_counts": dict(
            sorted(species_gene_counts.items(), key=lambda x: -x[1])[:15]
        ),
        "total_genes": sum(species_gene_counts.values()),
        "total_species": len(species_gene_counts),
        "total_annotations": total_annotations,
    }


ACTION_COLORS = {
    "ACCEPT": "#22c55e",
    "KEEP_AS_NON_CORE": "#60a5fa",
    "MODIFY": "#f59e0b",
    "REMOVE": "#ef4444",
    "MARK_AS_OVER_ANNOTATED": "#f97316",
    "UNDECIDED": "#a78bfa",
    "NEW": "#06b6d4",
    "PENDING": "#94a3b8",
    "NO_REVIEW": "#cbd5e1",
}

ACTION_ORDER = [
    "ACCEPT",
    "KEEP_AS_NON_CORE",
    "MODIFY",
    "REMOVE",
    "MARK_AS_OVER_ANNOTATED",
    "UNDECIDED",
    "NEW",
    "PENDING",
    "NO_REVIEW",
]


def generate_html(stats: dict) -> str:
    actions = stats["action_counts"]
    max_count = max(actions.values()) if actions else 1

    # Build bar chart rows
    bar_rows = ""
    for action in ACTION_ORDER:
        count = actions.get(action, 0)
        if count == 0:
            continue
        color = ACTION_COLORS.get(action, "#94a3b8")
        pct = count / max_count * 100
        label = action.replace("_", " ").title()
        bar_rows += f"""
        <div class="bar-row">
          <div class="bar-label">{label}</div>
          <div class="bar-track">
            <div class="bar-fill" style="width:{pct:.1f}%;background:{color}"></div>
          </div>
          <div class="bar-count">{count:,}</div>
        </div>"""

    # Build species table rows
    species_rows = ""
    for species, count in stats["species_gene_counts"].items():
        species_rows += f"<tr><td>{species}</td><td>{count}</td></tr>\n"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gene Review Dashboard</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
         background:#f1f5f9; color:#1e293b; padding:24px; }}
  .dashboard {{ max-width:900px; margin:0 auto; }}
  h1 {{ font-size:1.5rem; margin-bottom:4px; }}
  .subtitle {{ color:#64748b; font-size:0.9rem; margin-bottom:20px; }}
  .stats-row {{ display:flex; gap:12px; margin-bottom:20px; flex-wrap:wrap; }}
  .stat-card {{ background:white; border-radius:10px; padding:16px 20px; flex:1; min-width:140px;
               box-shadow:0 1px 3px rgba(0,0,0,0.08); text-align:center; }}
  .stat-value {{ font-size:1.8rem; font-weight:700; color:#3b82f6; }}
  .stat-label {{ font-size:0.75rem; color:#64748b; text-transform:uppercase; letter-spacing:0.05em; }}
  .card {{ background:white; border-radius:10px; padding:20px; margin-bottom:16px;
          box-shadow:0 1px 3px rgba(0,0,0,0.08); }}
  .card h2 {{ font-size:1.1rem; margin-bottom:14px; color:#334155; }}
  .bar-row {{ display:flex; align-items:center; gap:8px; margin-bottom:6px; }}
  .bar-label {{ width:160px; font-size:0.8rem; text-align:right; color:#475569; flex-shrink:0; }}
  .bar-track {{ flex:1; background:#f1f5f9; border-radius:4px; height:22px; overflow:hidden; }}
  .bar-fill {{ height:100%; border-radius:4px; transition:width 0.5s ease; }}
  .bar-count {{ width:60px; font-size:0.8rem; color:#64748b; text-align:right; font-variant-numeric:tabular-nums; }}
  table {{ width:100%; border-collapse:collapse; font-size:0.85rem; }}
  th {{ text-align:left; padding:6px 8px; border-bottom:2px solid #e2e8f0; color:#64748b; font-weight:600; }}
  td {{ padding:5px 8px; border-bottom:1px solid #f1f5f9; }}
  tr:hover td {{ background:#f8fafc; }}
</style>
</head>
<body>
<div class="dashboard">
  <h1>AI Gene Review Dashboard</h1>
  <p class="subtitle">Annotation review status across all genes</p>

  <div class="stats-row">
    <div class="stat-card">
      <div class="stat-value">{stats['total_genes']:,}</div>
      <div class="stat-label">Genes</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{stats['total_annotations']:,}</div>
      <div class="stat-label">Annotations</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{stats['total_species']}</div>
      <div class="stat-label">Species</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{actions.get('ACCEPT', 0):,}</div>
      <div class="stat-label">Accepted</div>
    </div>
  </div>

  <div class="card">
    <h2>Annotations by Review Action</h2>
    {bar_rows}
  </div>

  <div class="card">
    <h2>Top Species by Gene Count</h2>
    <table>
      <thead><tr><th>Species</th><th>Genes</th></tr></thead>
      <tbody>{species_rows}</tbody>
    </table>
  </div>
</div>
</body>
</html>"""


if __name__ == "__main__":
    stats = collect_stats()
    html = generate_html(stats)
    out = Path("pages/dashboard.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print(f"Dashboard written to {out} ({stats['total_genes']} genes, {stats['total_annotations']} annotations)")

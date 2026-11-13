"""Render the per-entry alignment table from an align_audit report.

Usage, from the ai-gene-review root:

    uv run python projects/DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/make_table.py \
        projects/DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/report-baseline.yaml

The report is produced by the audit script of the metabolic alignment project,
run over this project's scope:

    DISMECH_DIR=../dismech AIGR_TREE="<what the tree is>" \
    uv run python projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py \
        projects/DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/scope.yaml \
        projects/DISMECH_SYNAPTIC_VESICLE_ALIGNMENT/<report>.yaml

Prints a Markdown table to stdout. Nothing here is hand-entered: every cell is
read from the report, so the page table can be regenerated instead of trusted.
"""
import sys

import yaml

report = yaml.safe_load(open(sys.argv[1]))
prov = report["provenance"]

print(
    f"Run `{prov['run_date']}`; dismech `{prov['dismech_revision'][:9]}`; "
    f"ai-gene-review `{prov['aigr_revision'][:9]}` ({prov['aigr_tree']}); "
    f"GO `{prov['go_version']}`.\n"
)
print("| dismech entry | Gene | Relationship | Origin | Nodes naming gene | Review | Aligned node terms | Unmatched node terms | Modules | Flags |")
print("|---|---|---|---|---|---|---|---|---|---|")
for entry in report["entries"]:
    if entry.get("problem"):
        print(f"| {entry['entry']} | - | - | - | - | - | - | - | - | {entry['problem']} |")
        continue
    for g in entry.get("genes", []):
        aligned = ", ".join(f"`{t}`" for t in g.get("aligned_terms", [])) or "-"
        unmatched = ", ".join(f"`{t}`" for t in g.get("dismech_only", [])) or "-"
        modules = ", ".join(g.get("modules", [])) or "-"
        flags = ", ".join(f"`{f}`" for f in g.get("flags", [])) or "ok"
        print(
            f"| {entry['entry']} | {g['gene']} | {g.get('relationship') or '-'} | {g.get('origin') or '-'} "
            f"| {g.get('nodes', 0)} | {g.get('aigr_status', 'none')} | {aligned} | {unmatched} | {modules} | {flags} |"
        )

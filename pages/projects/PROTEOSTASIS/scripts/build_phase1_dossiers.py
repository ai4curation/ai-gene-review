#!/usr/bin/env python3
"""Build per-gene PN dossiers for the phase1 consistency review.

For each reviewed gene (from review_batches.tsv) assemble:
  - PN workbook rows (MAIN sheet): Branch/Class/Group/Type/Subtype + domains + notes + ref titles
  - The PN-taxonomy-node mapping record(s) for the gene's full path and each ancestor prefix
    (subject_curations across mappings/*.yaml): curation_status, scope, target GO, rationale
  - Projected GO annotations for the gene (pn_projected_annotations.tsv), if any

Outputs one markdown dossier per gene to reports/phase1_dossiers/<GENE>.md
and prints a summary.
"""
import yaml, glob, os, sys, csv
import pandas as pd
from collections import defaultdict

ROOT = "projects/PROTEOSTASIS"
WB = f"{ROOT}/references/proteostasis_network_annotation_4_3_11_2026_0417.xlsx"
OUT = f"{ROOT}/reports/phase1_dossiers"
os.makedirs(OUT, exist_ok=True)

# 1. reviewed genes
genes = []
with open(f"{ROOT}/review_batches.tsv") as fh:
    r = csv.DictReader(fh, delimiter="\t")
    for row in r:
        genes.append((row["gene_symbol"], row["batch_id"], row["review_yaml_path"]))
gene_batch = {g: (b, p) for g, b, p in genes}
gene_list = sorted(gene_batch)

# 2. workbook MAIN rows per gene
df = pd.read_excel(WB, sheet_name="MAIN")
REFCOLS = [c for c in df.columns if str(c).startswith("REF")]
wb_rows = defaultdict(list)
for _, r in df.iterrows():
    sym = r["Gene Symbol"]
    if pd.isna(sym):
        continue
    wb_rows[str(sym).strip()].append(r)

# 3. mapping index: subject_code -> [(file, rec)]
midx = defaultdict(list)
for f in glob.glob(f"{ROOT}/mappings/*.yaml"):
    data = yaml.safe_load(open(f))
    for rec in data.get("subject_curations", []):
        midx[rec.get("subject_code")].append((os.path.basename(f), rec))

# 4. projected annotations per gene
proj = defaultdict(list)
pf = f"{ROOT}/reports/pn_projection/pn_projected_annotations.tsv"
with open(pf) as fh:
    r = csv.DictReader(fh, delimiter="\t")
    for row in r:
        proj[row["gene_symbol"]].append(row)


def path_parts(r):
    parts = []
    for col in ["Branch", "Class", "Group", "Type", "Subtype"]:
        v = r.get(col)
        if pd.isna(v):
            continue
        v = str(v).strip()
        if not v or v.startswith("(no "):
            continue
        parts.append(v)
    return parts


def fmt_val(v):
    return "" if pd.isna(v) else str(v).strip()


summary = []
for g in gene_list:
    lines = [f"# PN dossier: {g}", ""]
    batch, ypath = gene_batch[g]
    lines.append(f"- review_batch: {batch}")
    lines.append(f"- review_yaml: {ypath}")
    rows = wb_rows.get(g, [])
    lines.append(f"- PN workbook rows: {len(rows)}")
    lines.append("")
    n_map = 0
    for i, r in enumerate(rows, 1):
        parts = path_parts(r)
        lines.append(f"## PN row {i}: {' | '.join(parts)}")
        uid = fmt_val(r.get("UniProt ID")); 
        if uid: lines.append(f"- UniProt: {uid}")
        inb = fmt_val(r.get("In branches"))
        if inb: lines.append(f"- In branches: {inb}")
        sig = fmt_val(r.get("Signature domains "))
        aux = fmt_val(r.get("Auxiliary Domains"))
        if sig: lines.append(f"- Signature domains: {sig}")
        if aux: lines.append(f"- Auxiliary domains: {aux}")
        notes = fmt_val(r.get("Notes"))
        if notes: lines.append(f"- Notes: {notes}")
        refs = [fmt_val(r.get(c)) for c in REFCOLS if fmt_val(r.get(c))]
        if refs:
            lines.append("- PN references (titles):")
            for rf in refs:
                lines.append(f"    - {rf}")
        # mapping records for full path + ancestors
        lines.append("- PN-node mapping records (path + ancestors):")
        for j in range(len(parts), 0, -1):
            code = "|".join(parts[:j])
            if code in midx:
                for fn, rec in midx[code]:
                    tt = rec.get("target_term") or {}
                    go = f"{tt.get('id','')} {tt.get('label','')}".strip()
                    st = rec.get("curation_status")
                    sc = rec.get("mapping_scope") or ""
                    if st == "mapped":
                        n_map += 1
                    lines.append(f"    - [{rec.get('subject_level')}] {code}")
                    lines.append(f"        status={st} scope={sc} GO=[{go}]")
                    rat = str(rec.get("rationale", "")).strip()
                    if rat:
                        lines.append(f"        rationale: {rat}")
        lines.append("")
    # projections
    pr = proj.get(g, [])
    if pr:
        lines.append(f"## Projected GO annotations ({len(pr)})")
        for row in pr:
            lines.append(f"- {row['target_go_id']} {row['target_go_label']} | scope={row['mapping_scope']} | goa_status={row['goa_status']} | from={row['mapping_subject_code']}")
        lines.append("")
    open(f"{OUT}/{g}.md", "w").write("\n".join(lines))
    summary.append((g, len(rows), len(pr), n_map))

print(f"Wrote {len(gene_list)} dossiers to {OUT}")
print("Genes with 0 workbook rows:", [g for g, nr, np_, nm in summary if nr == 0])
print("Genes with >=1 mapped PN node:", sum(1 for g, nr, np_, nm in summary if nm > 0))
print("Genes with projected GO:", sum(1 for g, nr, np_, nm in summary if np_ > 0))

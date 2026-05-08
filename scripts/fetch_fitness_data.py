#!/usr/bin/env python3
"""Fetch FEBA/RB-TnSeq mutant fitness data for a bacterial gene.

Data sources (tried in order):
1. Local FEBA SQLite database (~/repos/feba/cgi_data/feba.db)
2. Local FEBA HTML data directories (~/repos/feba with BarSeqR output TSVs)
3. FEBA bulk download TSVs from fit.genomics.lbl.gov (if available)

Outputs: genes/ORGANISM/GENE/GENE-fitness.md
"""

import csv
import io
import sqlite3
import sys
from pathlib import Path

# Known organism mappings: our org code -> FEBA orgId
ORGANISM_TO_FEBA = {
    "PSEPK": "Putida",
    "ECOLI": "keio",
    "SALTY": "SB2B",
}

FEBA_REPO = Path.home() / "repos" / "feba"
FEBA_DB = FEBA_REPO / "cgi_data" / "feba.db"


def find_feba_html_dir(org_id: str) -> Path | None:
    """Find the BarSeqR HTML output directory for an organism."""
    # BarSeqR output is typically in html/{orgId}/ with fit_logratios_good.tab etc.
    for parent in [FEBA_REPO / "html", FEBA_REPO / "htmlresults", FEBA_REPO]:
        candidate = parent / org_id
        if (candidate / "fit_logratios_good.tab").exists():
            return candidate
    return None


def query_sqlite(org_id: str, locus_tag: str) -> dict | None:
    """Query fitness data from the local FEBA SQLite database."""
    if not FEBA_DB.exists():
        return None

    conn = sqlite3.connect(str(FEBA_DB))
    conn.row_factory = sqlite3.Row

    # Look up gene info
    gene_row = conn.execute(
        "SELECT * FROM Gene WHERE orgId = ? AND (locusId = ? OR sysName = ? OR gene = ?)",
        (org_id, locus_tag, locus_tag, locus_tag),
    ).fetchone()
    if not gene_row:
        conn.close()
        return None

    locus_id = gene_row["locusId"]

    # Get fitness values with experiment descriptions
    fitness_rows = conn.execute(
        """SELECT gf.expName, gf.fit, gf.t, e.expDesc, e.expGroup,
                  e.condition_1, e.concentration_1, e.units_1,
                  e.condition_2, e.concentration_2, e.units_2,
                  e.media
           FROM GeneFitness gf
           JOIN Experiment e ON gf.orgId = e.orgId AND gf.expName = e.expName
           WHERE gf.orgId = ? AND gf.locusId = ?
           ORDER BY ABS(gf.t) DESC""",
        (org_id, locus_id),
    ).fetchall()

    # Get cofitness partners
    cofit_rows = conn.execute(
        """SELECT c.hitId, c.cofit, c.rank, g.sysName, g.gene, g.desc
           FROM Cofit c
           JOIN Gene g ON c.orgId = g.orgId AND c.hitId = g.locusId
           WHERE c.orgId = ? AND c.locusId = ?
           ORDER BY c.rank""",
        (org_id, locus_id),
    ).fetchall()

    # Get specific phenotypes
    specific_rows = conn.execute(
        """SELECT sp.expName, e.expDesc, e.expGroup
           FROM SpecificPhenotype sp
           JOIN Experiment e ON sp.orgId = e.orgId AND sp.expName = e.expName
           WHERE sp.orgId = ? AND sp.locusId = ?""",
        (org_id, locus_id),
    ).fetchall()

    conn.close()

    return {
        "gene": dict(gene_row),
        "fitness": [dict(r) for r in fitness_rows],
        "cofitness": [dict(r) for r in cofit_rows],
        "specific_phenotypes": [dict(r) for r in specific_rows],
    }


def read_tab_file(path: Path) -> list[dict]:
    """Read a tab-delimited file with header row."""
    rows = []
    with open(path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            rows.append(row)
    return rows


def query_html_dir(org_id: str, locus_tag: str) -> dict | None:
    """Query fitness data from BarSeqR HTML output TSV files."""
    html_dir = find_feba_html_dir(org_id)
    if not html_dir:
        return None

    fit_file = html_dir / "fit_logratios_good.tab"
    t_file = html_dir / "fit_t.tab"
    exps_file = html_dir / "expsUsed"

    if not all(f.exists() for f in [fit_file, t_file, exps_file]):
        return None

    # Read experiment metadata
    exps = {}
    for row in read_tab_file(exps_file):
        name = row.get("name", row.get("SetName", ""))
        exps[name] = row

    # Read fitness and t-score matrices
    fit_rows = read_tab_file(fit_file)
    t_rows = read_tab_file(t_file)

    # Find our gene
    gene_fit = None
    gene_t = None
    for i, row in enumerate(fit_rows):
        if row.get("locusId") == locus_tag or row.get("sysName", "") == locus_tag:
            gene_fit = row
            gene_t = t_rows[i] if i < len(t_rows) else None
            break

    if not gene_fit:
        return None

    # Build fitness entries (experiment columns start with "set")
    fitness = []
    exp_cols = [c for c in gene_fit if c.startswith("set")]
    for col in exp_cols:
        exp_name = col.split(" ")[0]  # strip annotations after name
        fit_val = gene_fit.get(col, "")
        t_val = gene_t.get(col, "") if gene_t else ""
        if not fit_val:
            continue
        exp_meta = exps.get(exp_name, {})
        fitness.append({
            "expName": exp_name,
            "fit": float(fit_val),
            "t": float(t_val) if t_val else 0.0,
            "expDesc": exp_meta.get("Description", exp_meta.get("SetName", exp_name)),
            "expGroup": exp_meta.get("Group", ""),
            "condition_1": exp_meta.get("Condition_1", ""),
            "concentration_1": exp_meta.get("Concentration_1", ""),
            "units_1": exp_meta.get("Units_1", ""),
            "media": exp_meta.get("Media", ""),
        })

    # Sort by |t| descending
    fitness.sort(key=lambda x: abs(x["t"]), reverse=True)

    # Read cofitness if available
    cofit_file = html_dir / "cofit"
    cofitness = []
    if cofit_file.exists():
        for row in read_tab_file(cofit_file):
            if row.get("locusId") == locus_tag:
                cofitness.append({
                    "hitId": row.get("hitId", ""),
                    "cofit": float(row.get("cofit", 0)),
                    "rank": int(row.get("rank", 0)),
                    "hitSysName": row.get("hitSysName", ""),
                    "hitName": row.get("hitName", ""),
                    "hitDesc": row.get("hitDesc", ""),
                })

    # Read gene info
    genes_file = html_dir / "genes"
    gene_info = {"locusId": locus_tag}
    if genes_file.exists():
        for row in read_tab_file(genes_file):
            if row.get("locusId") == locus_tag or row.get("sysName", "") == locus_tag:
                gene_info = row
                break

    return {
        "gene": gene_info,
        "fitness": fitness,
        "cofitness": cofitness,
        "specific_phenotypes": [],
    }


def try_bulk_download(org_id: str, locus_tag: str) -> dict | None:
    """Try to download fitness data from fit.genomics.lbl.gov bulk TSVs.

    The FEBA website may be behind Cloudflare protection, which blocks
    programmatic access. If this fails, the user should download the data
    manually or build the local SQLite database.
    """
    import urllib.request
    import urllib.error

    base_url = f"https://fit.genomics.lbl.gov/cgi-bin"

    # Try the gene fitness download endpoint
    fit_url = f"{base_url}/myFitShow.cgi?orgId={org_id}&gene={locus_tag}&format=tsv"
    try:
        req = urllib.request.Request(fit_url, headers={"User-Agent": "ai-gene-review/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            if "<!DOCTYPE html>" in content[:100].lower():
                # Got HTML instead of TSV — likely Cloudflare challenge
                return None
            reader = csv.DictReader(io.StringIO(content), delimiter="\t")
            fitness = []
            for row in reader:
                fitness.append({
                    "expName": row.get("name", ""),
                    "fit": float(row.get("fit", 0)),
                    "t": float(row.get("t", 0)),
                    "expDesc": row.get("short", row.get("desc", "")),
                    "expGroup": row.get("Group", ""),
                    "condition_1": row.get("Condition_1", ""),
                })
            fitness.sort(key=lambda x: abs(x["t"]), reverse=True)
            return {
                "gene": {"locusId": locus_tag},
                "fitness": fitness,
                "cofitness": [],
                "specific_phenotypes": [],
            }
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


def format_condition(row: dict) -> str:
    """Format an experiment condition string from a fitness row."""
    parts = []
    desc = row.get("expDesc", "")
    if desc:
        parts.append(desc)
    cond = row.get("condition_1", "")
    if cond and cond not in desc:
        conc = row.get("concentration_1", "")
        units = row.get("units_1", "")
        if conc and units:
            parts.append(f"{cond} {conc} {units}")
        elif conc:
            parts.append(f"{cond} {conc}")
        else:
            parts.append(cond)
    return " | ".join(parts) if parts else row.get("expName", "unknown")


def format_fitness_md(org_code: str, gene_symbol: str, org_id: str, data: dict) -> str:
    """Format fitness data as a markdown report."""
    gene = data["gene"]
    fitness = data["fitness"]
    cofitness = data["cofitness"]
    specific = data.get("specific_phenotypes", [])

    lines = [
        f"# FEBA/RB-TnSeq Fitness Data: {gene_symbol}",
        "",
        f"**Organism**: {org_code} (FEBA orgId: {org_id})",
        f"**Locus tag**: {gene.get('sysName', gene.get('locusId', gene_symbol))}",
    ]
    gene_name = gene.get("gene", "")
    if gene_name:
        lines.append(f"**Gene name**: {gene_name}")
    gene_desc = gene.get("desc", "")
    if gene_desc:
        lines.append(f"**Description**: {gene_desc}")
    lines.append(f"**Total experiments**: {len(fitness)}")
    lines.append("")

    # Count significant phenotypes
    sig_neg = [f for f in fitness if f["t"] < -4]
    sig_pos = [f for f in fitness if f["t"] > 4]
    lines.append(f"**Significant fitness defects** (t < -4): {len(sig_neg)}")
    lines.append(f"**Significant fitness gains** (t > 4): {len(sig_pos)}")
    lines.append("")

    # Interpretation summary
    lines.append("## Interpretation")
    lines.append("")
    if not fitness:
        lines.append("No fitness data available for this gene.")
    elif not sig_neg and not sig_pos:
        lines.append(
            "No strong fitness phenotypes detected across all conditions tested. "
            "This may indicate functional redundancy, the gene may be essential "
            "(and thus not represented in the mutant library), or the relevant "
            "condition was not tested."
        )
    else:
        if sig_neg:
            lines.append(f"**{len(sig_neg)} conditions** show significant fitness defects, suggesting:")
            # Group by experiment group if available
            groups = {}
            for f in sig_neg[:20]:
                grp = f.get("expGroup", "other")
                groups.setdefault(grp, []).append(f)
            for grp, entries in sorted(groups.items(), key=lambda x: -len(x[1])):
                conds = [format_condition(e) for e in entries[:5]]
                lines.append(f"- **{grp}**: {', '.join(conds)}")
            lines.append("")
        if sig_pos:
            lines.append(f"**{len(sig_pos)} conditions** show fitness gains with gene disruption.")
            lines.append("")

    # Top fitness phenotypes table
    lines.append("## Top Fitness Phenotypes")
    lines.append("")
    lines.append("Showing experiments with strongest fitness effects (|t| > 4):")
    lines.append("")
    lines.append("| Condition | Fitness | t-score | Group |")
    lines.append("|-----------|---------|---------|-------|")

    shown = 0
    for f in fitness:
        if abs(f["t"]) <= 4 and shown >= 10:
            break
        cond = format_condition(f)
        group = f.get("expGroup", "")
        lines.append(f"| {cond} | {f['fit']:.2f} | {f['t']:.1f} | {group} |")
        shown += 1
        if shown >= 30:
            remaining = len([x for x in fitness if abs(x["t"]) > 4]) - shown
            if remaining > 0:
                lines.append(f"| ... and {remaining} more significant phenotypes | | | |")
            break
    lines.append("")

    # Specific phenotypes
    if specific:
        lines.append("## Specific Phenotypes")
        lines.append("")
        lines.append("These are conditions where this gene shows a specific (non-generic) phenotype:")
        lines.append("")
        for sp in specific:
            desc = sp.get("expDesc", sp.get("expName", ""))
            group = sp.get("expGroup", "")
            lines.append(f"- {desc} ({group})")
        lines.append("")

    # Cofitness partners
    if cofitness:
        lines.append("## Top Cofitness Partners")
        lines.append("")
        lines.append(
            "Genes with highly correlated fitness profiles (cofitness > 0.5 suggests "
            "shared pathway or complex):"
        )
        lines.append("")
        lines.append("| Rank | Locus | Gene | Cofitness | Description |")
        lines.append("|------|-------|------|-----------|-------------|")
        for cf in cofitness[:20]:
            locus = cf.get("hitSysName", cf.get("hitId", ""))
            name = cf.get("hitName", cf.get("gene", ""))
            desc = cf.get("hitDesc", cf.get("desc", ""))
            lines.append(f"| {cf.get('rank', '')} | {locus} | {name} | {cf['cofit']:.3f} | {desc} |")
        lines.append("")

    # Data source
    lines.append("## Data Source")
    lines.append("")
    lines.append(
        "Data from the Fitness Browser (fit.genomics.lbl.gov), based on RB-TnSeq "
        "experiments from the Deutschbauer lab. See: Wetmore et al. (2015) "
        "\"Rapid quantification of mutant fitness in diverse bacteria by sequencing "
        "randomly bar-coded transposons\" mBio 6:e00306-15."
    )
    lines.append("")
    lines.append("### How to interpret fitness values")
    lines.append("")
    lines.append("- **Fitness = 0**: No effect of gene disruption")
    lines.append("- **Fitness < -1** (t < -4): Gene is important for growth in this condition")
    lines.append("- **Fitness > 1** (t > 4): Gene disruption improves growth (possible regulatory role)")
    lines.append("- **Cofitness > 0.8**: Strong evidence for shared pathway/complex")
    lines.append("- **Cofitness 0.5-0.8**: Moderate evidence for functional relationship")
    lines.append("")

    return "\n".join(lines)


def resolve_locus_tag(org_code: str, gene_symbol: str, gene_dir: Path) -> str:
    """Resolve a gene symbol to a FEBA locus tag.

    For P. putida, locus tags are PP_NNNN. Check the UniProt file for
    OrderedLocusNames if the gene symbol isn't already a locus tag.
    """
    # If gene_symbol looks like a locus tag already, use it
    if gene_symbol.startswith("PP_") or gene_symbol.startswith("b") or "_" in gene_symbol:
        return gene_symbol

    # Try to extract locus tag from UniProt file
    uniprot_file = gene_dir / f"{gene_symbol}-uniprot.txt"
    if uniprot_file.exists():
        text = uniprot_file.read_text()
        for line in text.splitlines():
            if line.startswith("GN   OrderedLocusNames="):
                # Extract first locus tag
                rest = line.split("=", 1)[1]
                tag = rest.split()[0].rstrip(",;")
                if tag:
                    return tag
    return gene_symbol


def main():
    if len(sys.argv) < 3:
        print("Usage: fetch_fitness_data.py <organism> <gene>")
        print()
        print("Examples:")
        print("  python scripts/fetch_fitness_data.py PSEPK PP_0635")
        print("  python scripts/fetch_fitness_data.py PSEPK pedH")
        print()
        print("Known organism mappings:")
        for our_code, feba_id in sorted(ORGANISM_TO_FEBA.items()):
            print(f"  {our_code} -> {feba_id}")
        sys.exit(1)

    org_code = sys.argv[1]
    gene_symbol = sys.argv[2]

    org_id = ORGANISM_TO_FEBA.get(org_code)
    if not org_id:
        print(f"Warning: No FEBA organism mapping for '{org_code}'.")
        print(f"Known mappings: {ORGANISM_TO_FEBA}")
        print(f"Using '{org_code}' as FEBA orgId directly.")
        org_id = org_code

    gene_dir = Path("genes") / org_code / gene_symbol
    if not gene_dir.exists():
        print(f"Error: Gene directory {gene_dir} does not exist.", file=sys.stderr)
        print(f"Run 'just fetch-gene {org_code} {gene_symbol}' first.", file=sys.stderr)
        sys.exit(1)

    locus_tag = resolve_locus_tag(org_code, gene_symbol, gene_dir)
    print(f"Looking up fitness data for {org_id}/{locus_tag}...")

    # Try data sources in order
    data = query_sqlite(org_id, locus_tag)
    if data:
        print(f"Found data in local FEBA database ({FEBA_DB})")
    else:
        data = query_html_dir(org_id, locus_tag)
        if data:
            print(f"Found data in FEBA HTML directory")
        else:
            print("No local FEBA data found. Trying bulk download...")
            data = try_bulk_download(org_id, locus_tag)
            if data:
                print("Downloaded fitness data from fit.genomics.lbl.gov")

    if not data or not data["fitness"]:
        output_file = gene_dir / f"{gene_symbol}-fitness.md"
        output_file.write_text(
            f"# FEBA/RB-TnSeq Fitness Data: {gene_symbol}\n\n"
            f"No fitness data found for {org_id}/{locus_tag}.\n\n"
            f"Possible reasons:\n"
            f"- The FEBA database is not available locally (check ~/repos/feba/cgi_data/feba.db)\n"
            f"- No BarSeqR HTML output directories found\n"
            f"- The organism '{org_id}' may not be in the FEBA database\n"
            f"- The gene may be essential (no viable mutants in the library)\n\n"
            f"To set up local data, build the FEBA database:\n"
            f"  cd ~/repos/feba && perl bin/db_setup.pl -db cgi_data/feba.db ...\n"
        )
        print(f"No fitness data found. Wrote placeholder to {output_file}")
        sys.exit(0)

    md = format_fitness_md(org_code, gene_symbol, org_id, data)
    output_file = gene_dir / f"{gene_symbol}-fitness.md"
    output_file.write_text(md)
    print(f"Wrote fitness data to {output_file}")

    # Print summary
    n_sig = len([f for f in data["fitness"] if abs(f["t"]) > 4])
    n_cofit = len(data["cofitness"])
    print(f"  {len(data['fitness'])} experiments, {n_sig} significant phenotypes, {n_cofit} cofitness partners")


if __name__ == "__main__":
    main()

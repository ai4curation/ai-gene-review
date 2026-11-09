"""Survey of PANTHER PTHR13158 (NAD kinase 2, mitochondrial) membership and motifs.

Reproducible, network-backed analysis; nothing is hard-coded except query
parameters. Run from the repository root:

    uv run python interpro/panther/PTHR13158/PTHR13158-bioinformatics/family_survey.py

Outputs (written next to this script):
  reference_tree.tsv   every leaf of the PANTHER reference tree: leaf PTN, organism,
                       gene, subfamily, and the chain of ancestral PTN nodes, with a
                       flag for whether the leaf descends from the PAINT IBD nodes
                       PTN004406956 (NAD+ kinase activity, NAD+ metabolic process) and
                       PTN000994636 (mitochondrion).
  member_summary.tsv   UniProtKB members (all, reviewed + unreviewed) counted by
                       lineage group, PANTHER subfamily, NADK catalytic-motif class and
                       presence of the Pfam NAD_kinase domain (PF01513).
  nadk_paralogs.tsv    for selected model organisms, every UniProtKB entry in PTHR13158 or
                       PTHR20275 (the cytosolic NADK / Pos5 family), found by PANTHER
                       cross-reference (not gated on Pfam), with its subfamily and whether
                       it also carries Pfam PF01513.

Steps:
1. PANTHER treeinfo API (PANTHER 19) -> reference tree topology and subfamily nodes.
2. UniProtKB search (xref PANTHER PTHR13158), paginated -> lineage, subfamily, Pfam.
3. UniProtKB FASTA for the same query -> motif class. The canonical NAD kinase motif is
   GGDG followed by T (human NADK2 G159-G162, catalytic Asp161; PMID:35733246). Members
   are classed as GGDGT, GQDGL (the common bacterial variant), other G-x-D-G, or none.
   A regex search is a coarse proxy for an alignment: it can miss motifs that are
   present but substituted, so 'none' means 'no G-x-D-G found', not 'no active site'.
4. UniProtKB search per organism, xref:panther-PTHR13158 and xref:panther-PTHR20275
   -> NADK paralog inventory. Organisms that return no entry for either family are
   reported as dropped rather than silently omitted.
"""

from __future__ import annotations

import csv
import io
import json
import re
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
FAMILY = "PTHR13158"
IBD_ROOT = "PTN004406956"
IBD_MITO = "PTN000994636"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
MODEL_ORGANISMS = {
    "9606": "Homo sapiens",
    "10090": "Mus musculus",
    "7227": "Drosophila melanogaster",
    "6239": "Caenorhabditis elegans",
    "36329": "Plasmodium falciparum 3D7",
}


def fetch(url: str) -> tuple[str, dict]:
    """GET a URL and return (body, headers)."""
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review family survey"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode(), dict(r.headers)


def uniprot_paged(query: str, fmt: str, fields: str | None = None) -> str:
    """Return all pages of a UniProtKB search as one text blob (TSV header kept once)."""
    url = f"{UNIPROT}?query={query}&format={fmt}&size=500"
    if fields:
        url += f"&fields={fields}"
    out: list[str] = []
    first = True
    while url:
        body, headers = fetch(url)
        lines = body.splitlines(True)
        if fmt == "tsv" and not first:
            lines = lines[1:]
        out.extend(lines)
        first = False
        link = headers.get("Link") or headers.get("link") or ""
        m = re.search(r'<([^>]+)>; rel="next"', link)
        url = m.group(1) if m else ""
    return "".join(out)


def children(node: dict) -> list[dict]:
    """Child annotation nodes of a PANTHER treeinfo node."""
    c = node.get("children")
    if not c:
        return []
    c = c.get("annotation_node")
    return c if isinstance(c, list) else [c]


def tree_leaves(node: dict, path: list[str]) -> list[dict]:
    """Flatten the tree into leaf records carrying their ancestor PTN path."""
    pid = node.get("persistent_id", "")
    kids = children(node)
    if not kids:
        return [
            {
                "leaf_ptn": pid,
                "organism": node.get("organism", ""),
                "gene_symbol": node.get("gene_symbol") or "",
                "gene_id": node.get("gene_id", ""),
                "subfamily": node.get("prop_sf_id", ""),
                "ancestors": ">".join(path),
                "under_root_ibd": IBD_ROOT in path,
                "under_mito_ibd": IBD_MITO in path,
            }
        ]
    out: list[dict] = []
    for k in kids:
        out += tree_leaves(k, path + [pid] if pid else path)
    return out


def tree_internal(node: dict, depth: int = 0) -> list[str]:
    """Indented listing of internal nodes (taxon, event, subfamily)."""
    kids = children(node)
    if not kids:
        return []
    line = "  " * depth + " ".join(
        x
        for x in [
            node.get("persistent_id", ""),
            node.get("species", ""),
            node.get("event_type", ""),
            node.get("sf_id", ""),
            f"leaves={len(tree_leaves(node, []))}",
        ]
        if x
    )
    out = [line]
    for k in kids:
        out += tree_internal(k, depth + 1)
    return out


def lineage_group(lineage: str) -> str:
    """Coarse lineage bucket for a UniProt 'Taxonomic lineage' string."""
    for name in ["Metazoa", "Fungi", "Viridiplantae", "Bacteria", "Archaea"]:
        if re.search(rf"\b{name}\b", lineage):
            return name
    return "Other eukaryotes"


def motif_class(seq: str) -> str:
    """Class of the NAD kinase GGDG motif found in a sequence."""
    if "GGDGT" in seq:
        return "GGDGT"
    if "GQDGL" in seq:
        return "GQDGL"
    if re.search(r"G[^G]DG|GGDG", seq):
        return "other G-x-D-G"
    return "none"


def main() -> None:
    """Run all survey steps and write the TSV outputs."""
    body, _ = fetch(f"https://pantherdb.org/services/oai/pantherdb/treeinfo?family={FAMILY}")
    root = json.loads(body)["search"]["tree_topology"]["annotation_node"]
    leaves = tree_leaves(root, [])
    with open(HERE / "reference_tree.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(leaves[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(leaves)
    print("## PANTHER reference tree (internal nodes)")
    print("\n".join(tree_internal(root)))
    print(f"\nleaves: {len(leaves)}")
    print(f"leaves under {IBD_ROOT}: {sum(x['under_root_ibd'] for x in leaves)}")
    print(f"leaves under {IBD_MITO}: {sum(x['under_mito_ibd'] for x in leaves)}")
    print("leaves under the root IBD node but outside the mitochondrion IBD node:")
    for x in leaves:
        if x["under_root_ibd"] and not x["under_mito_ibd"]:
            print("  ", x["leaf_ptn"], x["organism"], x["gene_symbol"], x["gene_id"], x["subfamily"])
    print("leaves in SF4:")
    for x in leaves:
        if x["subfamily"].endswith("SF4"):
            print("  ", x["leaf_ptn"], x["organism"], x["gene_symbol"], x["gene_id"])

    tsv = uniprot_paged(
        f"xref:panther-{FAMILY}", "tsv", "accession,reviewed,organism_name,lineage,xref_panther,xref_pfam"
    )
    rows = list(csv.DictReader(io.StringIO(tsv), delimiter="\t"))
    fasta = uniprot_paged(f"xref:panther-{FAMILY}", "fasta")
    seqs: dict[str, str] = {}
    cur = ""
    for line in fasta.splitlines():
        if line.startswith(">"):
            cur = line.split("|")[1]
            seqs[cur] = ""
        else:
            seqs[cur] += line.strip()
    human = seqs.get("Q4G0N4", "")
    i = human.find("GGDGT")
    if i < 0:
        print("\nhuman NADK2 Q4G0N4 GGDGT motif: absent (or sequence not retrieved)")
    else:
        print(f"\nhuman NADK2 Q4G0N4 GGDGT motif at {i + 1}-{i + 5}: {human[i - 6:i + 10]}")
    counts: Counter = Counter()
    for r in rows:
        sf = next((p for p in r["PANTHER"].split(";") if ":SF" in p), "none")
        counts[
            (
                lineage_group(r["Taxonomic lineage"]),
                sf,
                motif_class(seqs.get(r["Entry"], "")),
                "PF01513" in r["Pfam"],
            )
        ] += 1
    with open(HERE / "member_summary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["lineage_group", "subfamily", "motif_class", "has_PF01513", "n_members"])
        for k, v in sorted(counts.items()):
            w.writerow([*k, v])
    print(f"\n## UniProtKB members: {len(rows)} (reviewed: {sum(r['Reviewed'] == 'reviewed' for r in rows)})")
    for k, v in sorted(counts.items()):
        print("  ", *k, v)

    pf = Counter()
    for k, v in counts.items():
        pf[(k[0], k[1], k[3])] += v
    print("\n## Pfam PF01513 (NAD_kinase) coverage by lineage and subfamily")
    for lg, sfam in sorted({(a, b) for a, b, _ in pf}):
        yes, no = pf[(lg, sfam, True)], pf[(lg, sfam, False)]
        print(f"   {lg} {sfam}: {yes}/{yes + no} with PF01513 ({100 * yes / (yes + no):.0f}%)")

    para_rows = []
    print("\n## NADK paralog inventory per model organism (by PANTHER cross-reference)")
    for taxid, name in MODEL_ORGANISMS.items():
        found = 0
        for fam_query in ["PTHR13158", "PTHR20275"]:
            t = uniprot_paged(
                f"organism_id:{taxid}+AND+xref:panther-{fam_query}", "tsv", "accession,gene_names,xref_panther,xref_pfam"
            )
            entries = list(csv.DictReader(io.StringIO(t), delimiter="\t"))
            found += len(entries)
            genes = sorted({(r["Gene Names"].split() or ["?"])[0] for r in entries})
            subfams = Counter(
                next((p for p in r["PANTHER"].split(";") if p.startswith(fam_query + ":SF")), fam_query) for r in entries
            )
            print(f"   {name} (taxid {taxid}) {fam_query}: {len(entries)} entries; genes {genes}; subfamilies {dict(subfams)}")
            for r in entries:
                para_rows.append(
                    {
                        "organism": name,
                        "taxid": taxid,
                        "family_query": fam_query,
                        "accession": r["Entry"],
                        "gene": r["Gene Names"],
                        "panther_subfamily": next(
                            (p for p in r["PANTHER"].split(";") if p.startswith(fam_query + ":SF")), ""
                        ),
                        "has_PF01513": "PF01513" in r["Pfam"],
                    }
                )
        if found == 0:
            print(f"   DROPPED: {name} (taxid {taxid}) returned no entry for either family")
    if not para_rows:
        raise SystemExit("No paralog entries returned for any organism; UniProt query failed?")
    with open(HERE / "nadk_paralogs.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(para_rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(para_rows)

if __name__ == "__main__":
    main()
